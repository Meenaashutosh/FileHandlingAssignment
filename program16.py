#16.Write a Python program to remove newline characters from a file


def remove_newline(fname):  
    list = open(fname).readlines()  
    return [str.rstrip('\n') for str in list]  
  
print(remove_newline("file.txt"))  
