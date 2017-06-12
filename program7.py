#7. Write a Python program to read a file line by line store it into an array

array = []
with open("file.txt","r") as text:
    for lines in text:
        array.append(lines)
    print(array)

#output
'''
[ashutoshmeena111@demo-1 FileHandlingAssignment]$ python program7.py
['redmi\n', 'apple\n', 'appo\n', 'moto\n', 'panasonic\n', 'sony\n', 'vivo\n']
'''
