from random import randrange

num_ips = 100
output_file = open('ips.txt', 'w')

not_valid = [10,127,169,172,192]
 
for n in range(num_ips):
    first = randrange(1,256)
    while first in not_valid:
    	first = randrange(1,256)
 
    ip = ".".join([str(first),str(randrange(1,256)),
    str(randrange(1,256)),str(randrange(1,256))])
    output_file.write(ip + '\n')