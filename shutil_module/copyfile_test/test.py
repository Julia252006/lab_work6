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


def safe_rfile(name):
    if os.path.isfile(name):
        f = open(name, 'r')
        print(f.read())
        f.close()


src_dir_path = cur_package_path() + 'files/src/'
safe_mkdir(src_dir_path)

src_file_name = src_dir_path + 'source.txt'
safe_mkfile(src_file_name, "Source file text.\nLet's test its copying!!\n")

dest_dir_path = cur_package_path() + 'files/dest/'
safe_mkdir(dest_dir_path)

dest_file_name = dest_dir_path + 'source_copy.txt'
shutil.copyfile(src_file_name, dest_file_name)

safe_rfile(dest_file_name)