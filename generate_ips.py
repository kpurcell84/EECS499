# Generates NUM_IPS random IP addresses

from random import randrange

NUM_IPS = 10000

def generate(num_ips):
	
	OUTPUT_FILE = open('random_ips.txt', 'w')

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
    generate(NUM_IPS)