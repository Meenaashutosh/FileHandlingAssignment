#1.Write a Python program to read an entire text file and print its contents.

# creating text file 
file = open("text.txt","wr+") 
print "file is created",file.name
# file containg data
file.write("Hello World,how are you................\nTheir is Award function in zensar") 

#reading data from file using read line
file.seek(0,0)

print (file.read())
file.close()

