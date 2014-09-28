Contains code for EECS 499 research with Professor Halderman

## To Run Traceroutes: 
	Set parameters in the three scripts below as desired, then
	`python generate_ips.py`
	`python traceroute_test.py`
	`python process_results.py`

## Notes:
	- If number of processes or -N value of traceroute (simultaneous packets sent) is set too high, buffer space runs out ("send probe: No buffer space available") and results are corrupted