# Processes results.out file to reveal totals

import sys

def process(infile):
	INPUT_FILE = open(infile,'r')
	valid_results = 0.0
	total_results = 0.0
	hop_sum = 0.0
	valid_hop_sum = 0.0
	time_sum = 0.0

	result = INPUT_FILE.readline().rstrip('\n')
	while result:
		result = result.split(', ')
		# print result

		if result[1] != 'NOTREACHED':
			hop_sum += float(result[1])
			valid_hop_sum += float(result[2])
			time_sum += float(result[4])
			valid_results += 1

		total_results += 1

		result = INPUT_FILE.readline().rstrip('\n')

	percent_valid = (valid_results/total_results)*100
	if valid_results == 0:
		print "No valid results"
		exit(1)
	avg_hops = hop_sum/valid_results
	avg_valid_hops = valid_hop_sum/valid_results
	avg_time = time_sum/valid_results
	print str("%.2f" % percent_valid) + '% valid results'
	print "Average hops: " + str(avg_hops)
	print "Average valid hops: " + str(avg_valid_hops)
	print "Average time: " + str(avg_time)

	INPUT_FILE.close()

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Specify an input file"
		exit(1)
	process(sys.argv[1])