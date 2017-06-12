#12.Write a Python program to copy the contents of a file to another file

from shutil import copyfile

import os

os.system("touch file.txt ")
copyfile('file.txt', 'file1.txt')
