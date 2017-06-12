#13.Write a  program to copy the contents of a file to another file

with open('ashu1.txt') as f1, open('ashu.txt') as f2:  
    for l1, l2 in zip(f1, f2):  
        # l1 from file1.txt, l2 from file.txt 
        print(l1+l2)  
