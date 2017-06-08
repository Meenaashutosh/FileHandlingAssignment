#1.Write a Python program to read an entire text file and print its contents.

# creating text file 
file = open("text.txt","w") 
print "file is created"
# file containg data
file.write("Hello World") 
file.write("Their is csr function in zensar") 
file.write("and all zensarian required to join it... ") 
file.write("why??? you can enjoy different activity in our organisation......") 
 
file.close() 

#reading data from file using read line
file = open("test.txt", "r") 
print file.readlines() 

