#7. Write a Python program to read a file line by line store it into an array

array = []
with open(''test1.txt'',"r") as file:
    for lines in file:
        array.append(lines)
    print(f_array)
