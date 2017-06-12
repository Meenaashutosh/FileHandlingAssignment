#5.Write a Python program to read a file line by line and store it into a list

def read_file(fname):
        with open(fname) as f2:
                
		#list is the list that contains the read lines.     
               	list = f2.readlines()            
		print(list)
read_file('file.txt')

#output
'''
[ashutoshmeena111@demo-1 FileHandlingAssignment]$ python program5.py
['redmi\n', 'apple\n', 'appo\n', 'moto\n', 'panasonic\n', 'sony\n', 'vivo\n']
'''
