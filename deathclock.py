from datetime import datetime
import time

enddate = datetime(year=2015, month=8, day=31, hour=23, minute=59, second=59)
now = datetime.now().replace(microsecond=0)

#print enddate
#print now

#diff = enddate - now

while datetime.now() < enddate:
	now = datetime.now().replace(microsecond=0)
	diff = enddate - now
	print diff
	time.sleep(1)

