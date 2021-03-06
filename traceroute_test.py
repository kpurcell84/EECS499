# Send traceroutes out to IP addresses in a file and process results 

# TODO:
#   Account for last line containing two hosts in same hop line

import os
import subprocess
import sys
import re
from multiprocessing import Pool

from process_results import process

INPUT_FILE = None
OUTPUT_FILE = None
PROCESSES = 1
PACKETS_PER_HOP = 2
MAX_HOPS = 80
SIM_PACKETS = 10
DEBUG = True

def is_ip(ip):
    a = ip.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

# Returns dictionary of results or empty dict if destination not reached
def parse_last_hop(last_hop, host):
	results = {}
	last_line = re.split(' +|ms|\n', last_hop)
	last_line = filter(None, last_line)

	# Check if last line contains target host
	reached_dest = False
	for num in last_line:
		if is_ip(num) and num == host:
			reached_dest = True
			break
		
	if not reached_dest:	
		return results

	results['hops'] = last_line[0]
	results['dest'] = host
	last_line.pop(0)

	time_sum = 0.0
	num_valid_packets = 0
	for num in last_line:
		# Check if it's a time value
		try:
			num = float(num)
		except ValueError:
			continue
		else:
			time_sum = time_sum + num
			num_valid_packets += 1
	results['time'] = time_sum/num_valid_packets
	return results

def is_valid_hop(hop):
	line = re.split(' +|ms|\n', hop)
	line = filter(None, line)

	if line[1] == '*':
		return False
	else:
		return True

def traceroute(host):
	proc = subprocess.Popen([ 'sudo', 'traceroute', host, '-n', '-q '+str(PACKETS_PER_HOP), '-m '+str(MAX_HOPS), '-N '+str(SIM_PACKETS) ], stdout=subprocess.PIPE)
	hop = ''
	valid_hops = 0
	while True:
		last_hop = hop
		hop = proc.stdout.readline()
		if not hop:
			break
		if is_valid_hop(hop):
			valid_hops += 1
		if DEBUG:
			print hop
	if DEBUG:
		print 'LASTHOP: ' + last_hop
	
	results = parse_last_hop(last_hop, host)
	results['host'] = host
	results['valid_hops'] = valid_hops-1
	
	proc.wait()

	return results

def write_results(results):
	if not 'dest' in results:
		OUTPUT_FILE.write(results['host'] + ', NOTREACHED\n')
	else:
		OUTPUT_FILE.write(results['host']+', '+str(results['hops'])+', '+str(results['valid_hops'])+', '+str(results['dest'])+', '+str(results['time'])+'\n')
		OUTPUT_FILE.flush()


########################################################################

pool = Pool(PROCESSES)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Usage: " + sys.argv[0] + " [hosts file] [results output file]"
		exit(1)
	INPUT_FILE = open(sys.argv[1],'r')
	OUTPUT_FILE = open(sys.argv[2], 'w')

	host = INPUT_FILE.readline().rstrip('\n')
	while host:
		pool.apply_async(traceroute, args=(host, ), callback=write_results)
		# write_results(traceroute(host))
		host = INPUT_FILE.readline().rstrip('\n')
	pool.close()
	pool.join()

	INPUT_FILE.close()
	OUTPUT_FILE.close()

	process('results.out')