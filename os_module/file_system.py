import os
import shutil

print('\n\t\t\tCurrent directory where script execute:\n\n', os.getcwd(), '\n')

print('\n\t\t\tChange script execution to parent dir\n')
os.chdir('..')

print('\n\t\t\t\'TEXT_DIR\' directory created\n')
os.mkdir('TEXT_DIR')

print("\n\t\t\tDirectories with path 'ONE/TWO/THREE‘) # Create tree of directories' created\n")
os.makedirs('ONE/TWO/THREE‘) # Create tree of directories')

print('\n\t\t\tGet list of contents for directory \'ONE\':\n', os.listdir('ONE'))

print('\n\t\t\tList of contents for executable directory\n', os.listdir('.'))

print('\n\n\t\t\t\'TEXT_DIR\' directory deleted\n')
os.rmdir('TEXT_DIR')
print('\n\t\t\t\'ONE\' directory tree deleted\n')
shutil.rmtree('ONE')