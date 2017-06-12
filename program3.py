#3.Write a Python program to append text to a file and display the text. 


def read_file(fname):  
        from itertools import islice  
        with open(fname, "w") as myfile:  
                myfile.write("Python Exercises\n")  
                myfile.write("Pratice")  
        txt = open(fname)  
        print(txt.read())  
read_file('file1.txt')  


#output
'''
[ashutoshmeena111@demo-1 FileHandlingAssignment]$ python program3.py
Python Exercises
Pratice
'''
