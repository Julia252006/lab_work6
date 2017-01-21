# Create a module with name my_os.py with next code implementation:
# 1. Print computer name, processor architecture
# 2. Print current work directory
# 3. Change work directory to “C:”
# 4. Print list of directories
# 5. Print list of files
# 6. For files check is it link or not
# 7. Back to initial work directory
# 8. Create “Temp” folder
# 9. Delete “Temp” folder

import os
import platform

# current working directory
cwd = os.path.abspath(".")

# Print computer name, processor architecture
print('computer name:', os.uname()[1])

# Print current work directory
print('processor architecture:', platform.processor())

# Change work directory to 'C:'
os.chdir('/home')
print('\n\t\tcurrent work directory:\n', os.getcwd())

# Print list of directories
print('\nlist of directories ({}):'.format(os.getcwd()),
     [directory for directory in os.listdir(".") if os.path.isdir(directory)])

# Print list of files
os.chdir('/')
print('\nlist of files ({}):'.format(os.getcwd()),
      [file for file in os.listdir(".") if os.path.isfile(file)])

# For files check is it link or not
os.chdir('/bin')
print('\nfilter of links ({}):'.format(os.getcwd())),
for file in os.listdir("."):
    if os.path.islink(file):
       print('\t\t', file, '-----> is link!')
    else:
        print('\t\t', file)

# Back to initial work directory
os.chdir(cwd)

# Create “Temp” folder
print('\n\'Temp\' directory created!\n')
os.mkdir('Temp')

# Delete “Temp” folder
print('\n\'Temp\' directory deleted!\n')
os.rmdir('Temp')