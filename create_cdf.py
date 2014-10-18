# Create a cdf graph based on number of hops in a traceroute test run

import sys
from scipy.stats import norm
import pylab
import numpy

from bisect import bisect_left
from array import array

def graph(infile, outfile):
	INPUT_FILE = open(infile,'r')
	OUTPUT_FILE = open(outfile, 'w')

	result = INPUT_FILE.readline().rstrip('\n')
	hops_list = []
	while result:
		result = result.split(', ')
		# print result

		if result[1] != 'NOTREACHED':
			hops_list.append(int(result[2]))
		result = INPUT_FILE.readline().rstrip('\n')

	hops_list.sort()
	print str(len(hops_list)) + " hosts reached"

	cur_i = hops_list[0]
	for idx, hop_num in enumerate(hops_list):
		while hop_num > cur_i:
			OUTPUT_FILE.write(str(cur_i) + ',' + str(idx/float(len(hops_list))) + '\n')
			cur_i += 1
		if idx == len(hops_list)-1:
			OUTPUT_FILE.write(str(cur_i) + ',' + str((idx+1)/float(len(hops_list))) + '\n')


	# print hops_list

	# a = numpy.array(hops_list)
	# num_bins = len(list(set(hops_list)))+3
	# counts, bin_edges = numpy.histogram(a, bins=num_bins, normed=True)
	# cdf = numpy.cumsum(counts)
	# pylab.plot(bin_edges[1:], cdf)

	# pylab.show()

	INPUT_FILE.close()

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Usage: " + sys.argv[0] + " [input results file] [output csv file]"
		exit(1)
	graph(sys.argv[1], sys.argv[2])