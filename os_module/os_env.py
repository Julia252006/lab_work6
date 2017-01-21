import os

print('\n\t\t\tSystem paths:\n\n', os.environ['PATH'])

print('\n\t\t\tSystem variables names:\n')
for key in os.environ.keys():
    print(key)