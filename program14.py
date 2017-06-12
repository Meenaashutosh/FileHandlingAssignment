#14.Write a Python program to read a random line from a file

import random
lines = open("ashu.txt").read().splitlines()
print random.choice(lines)


#output
'''
[ashutoshmeena111@demo-1 FileHandlingAssignment]$ python program14.py
How would I Pythonicly scale these values so that A[0] = 0 and A[3] = 100 
'''
