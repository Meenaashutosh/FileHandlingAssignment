#16.Write a Python program to remove newline characters from a file


def remove(fname):  
    list = open(fname).readlines()  
    return [str.rstrip('\n') for str in list]  
  
print(remove("file.txt"))  
