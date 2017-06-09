# Question 5:Write a Python program to read a file line by line and store it into a list

def file_read(fname):
        
	with open(fname) as f2:
                
		#list is the list that contains the read lines.     
                
		list = f2.readlines()
                
		print(list)


file_read('test.txt')
