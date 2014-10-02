# Create a cdf graph based on number of hops in a traceroute test run

import sys
from scipy.stats import norm
import pylab
import numpy

from bisect import bisect_left
from array import array

def graph(infile):
	INPUT_FILE = open(infile,'r')

	result = INPUT_FILE.readline().rstrip('\n')
	hops_list = []
	while result:
		result = result.split(', ')
		# print result

		if result[1] != 'NOTREACHED':
			hops_list.append(float(result[1]))
		result = INPUT_FILE.readline().rstrip('\n')

	# print hops_list

	a = numpy.array(hops_list)
	num_bins = len(list(set(hops_list)))+3
	counts, bin_edges = numpy.histogram(a, bins=num_bins, normed=True)
	cdf = numpy.cumsum(counts)
	pylab.plot(bin_edges[1:], cdf)

	pylab.show()

	INPUT_FILE.close()

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Specify an input file"
		exit(1)
	graph(sys.argv[1])