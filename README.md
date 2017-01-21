Brain Academy. Python Course. Laboratory Work #6.2

Create a module with name my_os.py with next code implementation:
 1. Print computer name, processor architecture
 2. Print current work directory
 3. Change work directory to “C:”
 4. Print list of directories
 5. Print list of files
 6. For files check is it link or not
 7. Back to initial work directory
 8. Create “Temp” folder
 9. Delete “Temp” folder
 
```python 
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
```
 
 
 
Brain Academy. Python Course. Laboratory Work #6.3

Create a module with name my_sys.py with next code implementation:
1. Print computer platform
2. Print installed computer python version
3. Check and print size of string object – “abc”
4. n variable should be received as script argument
5. n variable default value set as 11 in case of read sys argument fail
6. Use for loop and write every number item into system stdout flow
7. Do not use print statement for above task
8. In case of n%2 ==0 exit script execution with n code

```python 
import sys  # import sys module

print(sys.platform)
print(sys.version)
print(sys.getsizeof('abc'))

# n variable should be received as script argument
# n variable default value set as 11 in case of read sys argument fail
try:
    name, n = sys.argv  # Unpack into 2 variables name and n system arguments
except IndexError:
    n = 11  # Set default value

list_variable = list(range(0, int(n)))  # create list variable with number items from 0 to n

# use for loop and write every number item into system stdout flow
# do not use print statement for above task
for item in list_variable:
    sys.stdout.write(str(item) + ' ')  # Write every number item into system stdout flow

# in case of n%2 ==0 exit script execution with n code
if int(n) % 2 == 0:
    sys.exit(n)  # Exit script execution with n code


# PyCharm Terminal:
#
# cd ~/PycharmProjects/os/
# python3 work_6_3.py 10
```


Brain Academy. Python Course. Laboratory Work #6.4

Create a module with name my_argparse.py with next code implementation:
1. Check that executable script __name__ variable is equal to “__main__”
2. If yes print next:
3. String 'Parcer initialized!' and variables: lang, keyword and value
4. 3 variables are script arguments
5. Set coding of the script as “utf8”
6. Import argparse module
7. Create parser object
8. Add parser argument with key “–l”, string type, “ua” as default value 
   and add any help string for key. Store this value into lang variable
9. Add parser argument with key “–c”, string type, “word” as default value
   and add any help string for key. Store this value into keyword variable.
10.Add parser argument with key “–m”, integer type, “0” as default value
   and add any help string for key. Store this value into value variable.
   
```python 
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-l",'--lang', type=str, default='ua',
                    help= "Choose language abbreviation! (Ex. 'ua','en')")

parser.add_argument("-k", '--keyword', type=str, default='word',
                    help= "Choose word for filter! (Ex. 'hello')")

parser.add_argument("-v", '--value', type=int, default=0,
                    help= "Choose number of the best moody for tweets! (Ex. '10', '-12')")

# Check that executable script __name__ variable is equal to "__main__"
# If yes print next:
# 3 variables are script arguments

args = parser.parse_args()
lang = args.lang
keyword = args.keyword  # .encode('utf8')
value = args.value


if __name__ == '__main__':
    print('Parcer initialized!')
    print(lang, keyword, value)


# PyCharm Terminal:
#
# cd ~/PycharmProjects/os
# python3 work_6_4.py -l 'en' -k 'hello' -v '5'
# python3 work_6_4.py -l 'ua' -k 'привіт' -v '5'
```
   
   
Brain Academy. Python Course. Laboratory Work #6.5
Create a module with name my_shutil.py with next code implementation:
1. Create “folder_zip’ in current working directory
2. Create 3 files with an types of data in “folder_zip”
3. Archive “folder_zip” contents into one zip file with name “my_zip”
4. Copy “my_zip” into one folder above current
5. Remove folder “folder_zip” from disk
6. Add user prompt for checking folder state
7. Unpack archive in current folder
8. Print disk usage of folder were archive were copied


```python 
import os
import shutil


def cur_package_path():
    return str(__file__)[:str(__file__).rfind('/') + 1]


def safe_mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def safe_mkfile(name, content):
    if not os.path.isfile(name):
        f = open(name, 'w')
        f.write(content)
        f.close()

# 1. Create my_zip.zip file in current work directory
files_path = cur_package_path() + '/files'

safe_mkdir(files_path + '/folder_zip')
zip_dir_path = files_path + '/folder_zip'

# 2. Create files with data in current folder
for filename in range(3): \
    safe_mkfile(zip_dir_path + '/file_%s' % filename, 'some data')

# 3. Create my_zip.zip file in current work directory
shutil.make_archive("my_zip", "zip", root_dir=".",
                    base_dir="./files/folder_zip")
# 4. Copy archive into folder above
shutil.copy("my_zip.zip", "../my_zip.zip")

# 5. Remove folder_zip
shutil.rmtree(zip_dir_path)

input()
shutil.unpack_archive("../my_zip.zip")
os.remove("my_zip.zip")
os.remove("../my_zip.zip")
print(shutil.disk_usage("."))
```
