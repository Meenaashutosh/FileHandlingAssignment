#11.:Write a Python program to write a list to a file

mobile = ['redmi', 'apple', 'appo', 'moto', 'panasonic', 'sony','vivo']   
with open('file.txt', "w") as file:   
        for mob in mobile:   
                file.write("%s\n" % mob)   
   
content = open('file.txt')   
print(content.read())   


#output
'''
[ashutoshmeena111@demo-1 FileHandlingAssignment]$ python program11.py
redmi
apple
appo
moto
panasonic
sony
vivo
'''
