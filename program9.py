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
