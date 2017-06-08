# 2.Write a Python program to read first n lines of a file and print these lines.


def read_file(fname, nlines):  
        from itertools import islice  
        with open(fname) as f:  
                for line in islice(f, nlines):  
                        print(line)  
read_file('file.txt',3)



#output
'''
python program2.py
This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML.
Each has been recast in a form suitable for Python.
The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. 
'''
