import os
import shutil

files = os.listdir()
cur_dir = os.getcwd()
destinationpath = 'data'
for file in files:
    if file.endswith('.txt') or file.endswith('.json'):
        shutil.move(file, destinationpath)
