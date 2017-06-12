#13.Write a  program to copy the contents of a file to another file

with open('file1.txt') as fi1, open('file.txt') as fi2:  
    for l1, l2 in zip(fi1, fi2):  
        # l1 from file1.txt, l2 from file.txt 
        print(l1+l2)  
