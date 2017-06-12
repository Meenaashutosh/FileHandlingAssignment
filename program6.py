# 6.Write a Python program to read a file line by line store it into a variable


with open ("file.txt", "r") as file:
    var=file.readlines()
    print(var)

    
#output
'''
[ashutoshmeena111@demo-1 FileHandlingAssignment]$ python program6.py
['redmi\n', 'apple\n', 'appo\n', 'moto\n', 'panasonic\n', 'sony\n', 'vivo\n']
'''
