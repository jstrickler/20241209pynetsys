import os
import sys
import shutil
import logging

if sys.platform == 'win32':
    DEST = r'\TEMP'
else:
    DEST = '/tmp'

logging.basicConfig(
    filename='../TEMP/copying.log',
    level=logging.INFO,
)

for dir_path, dir_list, file_list in os.walk('../DATA'):
    for file_name in file_list:
        if file_name.endswith('.txt'):
            full_name = os.path.join(dir_path, file_name)
            message = f'copying {full_name} to {DEST}'
            print(message)
            logging.info(message)
            shutil.copy(full_name, DEST)
