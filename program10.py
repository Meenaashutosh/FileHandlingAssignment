#10.Write a Python program to get the file size of a plain file

import os 
str = os.stat('text.txt') 
print str.st_size 
 
#output
'''
[ashutoshmeena111@demo-1 FileHandlingAssignment]$ python program10.py
73
'''
