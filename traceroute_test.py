# Send traceroutes out to IP addresses in a file and process results 

# TODO:
#   Account for last line containing two hosts in same hop line

import os
import subprocess
import sys
import re
from multiprocessing import Pool

INPUT_FILE = open('ips.txt','r')
OUTPUT_FILE = open('results.out', 'w')
PROCESSES = 6
PACKETS_PER_HOP = 4
MAX_HOPS = 30

# Returns dictionary of results or None if destination not reached
def parse_last_hop(last_hop):
    results = {}
    last_line = re.split(' +|ms|\n', last_hop)
    last_line = filter(None, last_line)

    if last_line[1] == '*':
        return results

    results['hops'] = last_line[0]
    results['dest'] = last_line[1]
    last_line.pop(0)

    time_sum = 0.0
    num_valid_packets = 0
    for num in last_line:
        try:
            num = float(num)
        except ValueError:
            continue
        else:
            time_sum = time_sum + num
            num_valid_packets += 1
    results['time'] = time_sum/num_valid_packets
    return results

def traceroute(host):
    proc = subprocess.Popen([ 'traceroute', host, '-n', '-q '+str(PACKETS_PER_HOP), '-m '+str(MAX_HOPS) ], stdout=subprocess.PIPE)
    hop = ''
    while True:
        last_hop = hop
        hop = proc.stdout.readline()
        if not hop:
            break
        print hop
    print 'LASTHOP: ' + last_hop
    
    results = parse_last_hop(last_hop)
    results['host'] = host
    
    proc.wait()

    return results

def write_results(results):
    if not 'dest' in results:
        print 'NO RESULTS'
        OUTPUT_FILE.write(results['host'] + ', NOTREACHED\n')
    else:
        OUTPUT_FILE.write(results['host']+', '+str(results['hops'])+', '+str(results['dest'])+', '+str(results['time'])+'\n')


########################################################################

pool = Pool(PROCESSES)

if __name__ == '__main__':
    host = INPUT_FILE.readline().rstrip('\n')
    while host:
        print host
        pool.apply_async(traceroute, args=(host, ), callback=write_results)
        host = INPUT_FILE.readline().rstrip('\n')
    pool.close()
    pool.join()

INPUT_FILE.close()
OUTPUT_FILE.close()