# Create a module with name my_sys.py with next code implementation:
# 1. Print computer platform
# 2. Print installed computer python version
# 3. Check and print size of string object – “abc”
# 4. n variable should be received as script argument
# 5. n variable default value set as 11 in case of read sys argument fail
# 6. Use for loop and write every number item into system stdout flow
# 7. Do not use print statement for above task
# 8. In case of n%2 ==0 exit script execution with n code


import sys
print(sys.platform)
print(sys.version)
print(sys.getsizeof('abc'))

# n variable should be received as script argument
# n variable default value set as 11 in case of read sys argument fail
try:
    name, n = sys.argv
except IndexError:
    n = 11

list_variable = list(range(0, int(n)))

# use for loop and write every number item into system stdout flow
# do not use print statement for above task
for item in list_variable:
    sys.stdout.write(str(item) + ' ')

# in case of n%2 ==0 exit script execution with n code
if int(n) % 2 == 0:
    sys.exit(n)


# PyCharm Terminal:
#
# cd ~/PycharmProjects/os/
# python3 work_6_3.py 10
