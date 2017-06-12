#14.Write a Python program to read a random line from a file

import random
lines = open("ashu.txt").read().splitlines()
print random.choice(lines)
