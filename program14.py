#14.Write a Python program to read a random line from a file

import random_line
lines = open("text.txt").read().splitlines()
print random_line.choice(lines)
