# Create a module with name my_time.py with next code implementation:
# 1. Import time and datetime modules
# 2. After import statement set clock count for checking script execution time
# 3. Print current time in format 'Tue May 24 14:09:17 2016’
# 4. Print current time year
# 5.Print current time day from the year begining
# 6. Use time tuple convertion into string and create string line
#  with next format '24 Mar 2015 12:14‘
# 7. Use time convertion from string into time tuple
#  and create object from string '125 Jun. 1983 10:15'
# 8. Check the difference with datime delta
# 9. Print script execution time

import time
import datetime

time.clock()

print(time.ctime())
print(time.localtime().tm_year)
print(time.localtime().tm_yday)

print(time.strftime("%d %m. %Y %H:M",time.gmtime()))
print(datetime.datetime.strptime("25 Jun. 1983 10:15", "%d %b. %Y %H:%M"))
time_1 = datetime.datetime.now() + datetime.timedelta(days = -1)
now = datetime.datetime.now()
print('Time delta', (now - time_1).days)  # Check the difference with time delta

print("Script execution time: %f4.2" % time.clock())