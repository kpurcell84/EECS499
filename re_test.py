import re

last_hop = "19  221.183.9.202  281.914 ms 221.176.27.18  255.216 ms  251.873 ms 221.176.18.38  270.584 ms"
last_line = re.split(" +|ms|\n", last_hop)
last_line = filter(None, last_line)
for num in last_line:
	try: 
		float(num)
	except ValueError:
		pass
	else:
		print num

print last_line