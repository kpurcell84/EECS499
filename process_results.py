# Processes results.out file to reveal totals

def process():
    INPUT_FILE = open('results.out','r')
    valid_results = 0.0
    total_results = 0.0
    hop_sum = 0.0
    time_sum = 0.0

    result = INPUT_FILE.readline().rstrip('\n')
    while result:
        result = result.split(', ')
        # print result

        if result[1] != 'NOTREACHED':
            hop_sum += float(result[1])
            time_sum += float(result[3])
            valid_results += 1

        total_results += 1

        result = INPUT_FILE.readline().rstrip('\n')

    percent_valid = (valid_results/total_results)*100
    avg_hops = hop_sum/valid_results 
    avg_time = time_sum/valid_results
    print str("%.2f" % percent_valid) + '% valid results'
    print "Average hops: " + str(avg_hops)
    print "Average time: " + str(avg_time)

    INPUT_FILE.close()

if __name__ == '__main__':
    process()