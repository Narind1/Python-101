#write a program to print current date time using lan=mbda function in python

import datetime
format_datetime = lambda dt: dt.strftime("%B %d, %Y %I:%M:%S %p")
current_datetime = datetime.datetime.now()
print(format_datetime(current_datetime))