# Compare the results from two different test runs with the same list of hosts

import sys
from subprocess import call

def compare(infile1, infile2):
	# Sort files so IP addresses line up
	call(['sort', '-oresults1_s.out', infile1])
	call(['sort', '-oresults2_s.out', infile2])
	INPUT_FILE1 = open('results1_s.out','r')
	INPUT_FILE2 = open('results2_s.out','r')

	r1_reached = 0
	r2_reached = 0
	both_reached = 0
	neither_reached = 0
	r1_less_hops = 0
	r2_less_hops = 0
	equal_hops = 0

	result1 = INPUT_FILE1.readline().rstrip('\n')
	result2 = INPUT_FILE2.readline().rstrip('\n')

	while result1 and result2:
		result1 = result1.split(', ')
		result2 = result2.split(', ')

		if result1[0] != result2[0]:
			print "Trying to compare different hosts"
			exit(1)

		if result1[1] == 'NOTREACHED' and result2[1] == 'NOTREACHED':
			neither_reached += 1
		elif result1[1] != 'NOTREACHED' and result2[1] == 'NOTREACHED':
			r1_reached += 1
		elif result1[1] == 'NOTREACHED' and result2[1] != 'NOTREACHED':
			r2_reached += 1
		elif result1[1] != 'NOTREACHED' and result2[1] != 'NOTREACHED':
			both_reached += 1
			if int(result1[1]) < int(result2[1]):
				r1_less_hops += 1
			elif int(result1[1]) > int(result2[1]):
				r2_less_hops += 1
			else:
				equal_hops += 1

		result1 = INPUT_FILE1.readline().rstrip('\n')
		result2 = INPUT_FILE2.readline().rstrip('\n')

	print 'Only r1 reached: ' + str(r1_reached) + ' times'
	print 'Only r2 reached: ' + str(r2_reached) + ' times'
	print 'Neither reached: ' + str(neither_reached) + ' times'
	print 'Both reached: ' + str(both_reached) + ' times'
	print ''
	print 'r1 less hops than r2: ' + str(r1_less_hops) + ' times'
	print 'r2 less hops than r1: ' + str(r2_less_hops) + ' times'
	print 'r1 and r2 equal hops: ' + str(equal_hops) + ' times'

	INPUT_FILE1.close()
	INPUT_FILE2.close()


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Usage: " + sys.argv[0] + " [results file 1] [results file 2]"
		exit(1)
	compare(sys.argv[1], sys.argv[2])