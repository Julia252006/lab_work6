# Create a module with name my_shutil.py with next code implementation:
# 1. Create “folder_zip’ in current working directory
# 2. Create 3 files with an types of data in “folder_zip”
# 3. Archive “folder_zip” contents into one zip file with name “my_zip”
# 4. Copy “my_zip” into one folder above current
# 5. Remove folder “folder_zip” from disk
# 6. Add user prompt for checking folder state
# 7. Unpack archive in current folder
# 8. Print disk usage of folder were archive were copied

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