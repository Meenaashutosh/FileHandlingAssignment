# 2.Write a Python program to read first n lines of a file and print these lines.


def read_file(fname, nlines):  
        from itertools import islice  
        with open(fname) as f:  
                for line in islice(f, nlines):  
                        print(line)  
file_read('file.txt',3)
