#15. Write a Python program to assess if a file is closed or not

fi1=open("file.txt","r")
fi2=open("file.txt","r")
print(fi1.closed)
fi1.close()
print(fi2.closed)
fi2.close()
print(fi1.closed)
print(fi2.closed)
