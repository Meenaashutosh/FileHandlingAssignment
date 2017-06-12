#16.Write a Python program to remove newline characters from a file


def remove(fname):  
    list = open(fname).readlines()  
    return [str.rstrip('\n') for str in list]  
  
print(remove("file.txt"))  

#output
'''
[ashutoshmeena111@demo-1 FileHandlingAssignment]$ python program16.py
['<<<<<<< Updated upstream', 
'This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. ',
'Each has been recast  a form suitable for Python.', 
'The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. ', 
'Together, they form an \xe2\x80\x9citerator algebra\xe2\x80\x9d make it possible to construct specialized tools succinctly and efficiently in pure Python.',
'=======', 'redmi', 'apple', 'appo', 'moto', 'panasonic', 'sony', 'vivo', '>>>>>>> Stashed changes']
'''
