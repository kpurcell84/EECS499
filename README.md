Contains code for EECS 499 research with Professor Halderman

## To Run Traceroutes: 
Set parameters in the three scripts below as desired, then
`python generate_ips.py`
`python traceroute_test.py`

## Requirements:
- `pip install numpy`
- `pip install matplotlib`

## Notes:
- If number of processes, simultaneous packets sent, or max hops is set too high, buffer space runs out ("send probe: No buffer space available") and results are corrupted

## To do:
- Run large TCP and/or ICMP test (depending on results of small test) for ~2 days
- Make a CDF graph with number of hops on X-axis and % Reached (of successful responses) on Y-axis
- Add parameter for number of successful hops