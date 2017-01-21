# Create a module with name my_time.py with next code implementation:
# 1. Import time and datetime modules
# 2. After import statement set clock count for checking script execution time
# 3. Print current time in format 'Tue May 24 14:09:17 2016’
# 4. Print current time year
# 5.Print current time day from the year begining
# 6. Use time tuple convertion into string and create string line
#  with next format '24 Mar 2015 12:14‘
# 7. Use time convertion from string into time tuple
#  and create object from string '19 Sep. 2012 10:15'
# 8. Check the difference with datime delta
# 9. Print script execution time

import time  # import time module
import datetime  # import datetime module

time.clock()  # Set clock start

print(time.ctime())  # print current time in format 'Tue May 24 14:09:17 2016’
print(time.localtime().tm_year)  # Current time year
print(time.localtime().tm_yday)  # Current year day

print(time.strftime("%d %m. %Y %H:M",time.gmtime()))
print(datetime.datetime.strptime("25 Jun. 1983 10:15", "%d %b. %Y %H:%M"))
# time_1 = datetime.datetime.date(datetime.datetime.now().today() - 1)   # Create datetime tuple with current day minus one day
# datetime.timedelta(datetime.datetime.now() - time_1)  # Check the difference with datime delta

print("Script execution time:%f4.2"%time.clock())