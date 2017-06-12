# 9.Write a Python program to count the frequency of words in a file

file=open("file.txt","r+")

word_count={}

for word in file.read().split():
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

for l in word_count.items():
    print l
    
#output
'''
 python program9.py
 ('redmi', 1)
 ('apple', 1)
 ('vivo', 1)
 ('moto', 1)
 ('appo', 1)
 ('sony', 1)
 ('panasonic', 1)
 '''
