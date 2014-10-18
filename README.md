Contains code for EECS 499 research with Professor Halderman

## To Run Traceroutes: 
Set parameters in the three scripts below as desired, then
`python generate_ips.py`
`python traceroute_test.py`

## Requirements:


## Notes:
- If number of processes, simultaneous packets sent, or max hops is set too high, buffer space runs out ("send probe: No buffer space available") and results are corrupted

## To do:
- Design architecture for zmap traceroute extension
- Implement extension

## Done:
1. Created script to generate a specified amount of valid random IP addresses
2. Created a script to simultaneously send traceroutes to an inputted list of hosts and track the following:
	* Whether or not the destination was reached
	* Amount of valid hops to get there
	* Average time taken to get there
3.  Wrote another script to process results and get aggregate statistics such as number of times destination was reached, average hops, and average time taken
4.  Ran script with several different inputs to determine the optimal balance of processes, simultaneous packets, and max hops without overflowing buffer
5.  Ran script on 10,000 IPs in both ICMP and TCP mode to compare results
6.  Wrote a script to compare the result sets and see whether or not they were disjoint with respect to reaching the target host
7.	Ran traceroute script with 2,000,000 hosts for both ICMP and TCP on EECS server
8.	Graphed results as a CDF to determine optimal max hops setting