#1.Write a Python program to read an entire text file and print its contents.

# creating text file 
file = open("text.txt","wr+") 
print "file is created",file.name
# file containg data
file.write("Hello World") 
file.write("Their is csr function in zensar") 
file.write("and all zensarian required to join it... ") 
file.write("why??? you can enjoy different activity in our organisation......") 
 
#reading data from file using read line
file.seek(0,0)
line= file.read()
print (file.read())
file.close()

