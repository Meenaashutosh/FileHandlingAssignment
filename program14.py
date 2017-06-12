#14.Write a Python program to read a random line from a file

import random_line
lines = open(".txt").read().splitlines()
print random_line.choice(lines)
