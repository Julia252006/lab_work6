import os

print('\n\t\tos_module all attributes list:',
      os.stat('../os_module'), '\n')

print('\n\t\tos_module milliseconds time of its creating:',
      os.stat('../os_module').st_mtime, '\n')

print('\n\t\tfile_metadata.py all attributes list:',
      os.stat('file_metadata.py'))

os.rename('file_metadata.py', 'next_file_metadata.py')

os.rename('../os_module', '../system_os_module')