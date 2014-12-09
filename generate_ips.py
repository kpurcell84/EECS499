# Generates NUM_IPS random IP addresses

from random import randrange
import sys

def generate(num_ips, outfile):
	
	OUTPUT_FILE = open(outfile, 'w')

	NOT_VALID = [10,127,169,172,192]
	 
	for n in range(num_ips):
		first = randrange(1,256)
		while first in NOT_VALID:
			first = randrange(1,256)
	 
		ip = ".".join([str(first),str(randrange(1,256)),
		str(randrange(1,256)),str(randrange(1,256))])
		OUTPUT_FILE.write(ip + '\n')

	OUTPUT_FILE.close()

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Usage: " + sys.argv[0] + " [number of ips] [output file]"
		exit(1)
	generate(int(sys.argv[1]), sys.argv[2])