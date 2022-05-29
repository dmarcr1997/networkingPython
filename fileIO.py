from asyncore import write


myfile = open("./resources/routers.txt", "r")

print(myfile.mode)

print(myfile.read())

myfile.seek(0)
print(myfile.read(5))
print(myfile.tell())
myfile.seek(0)
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())

myfile.seek(0)
routers = myfile.readlines()
for router in routers:
    if(router.startswith('A')):
        print(router)
myfile.seek(0)

myfile.close()
print("Closed the router file")

# write

newfile = open("./resources/newfile.txt", 'w')
newfile.write("I like Python!\nDo you?")
newfile.close()
newfile = open("./resources/newfile.txt", 'r')
print(newfile.read())
newfile.close()

newfile = open('./resources/newfile.txt', "a")
newfile.write("this string was appended")
newfile.close()
#write and read use r+ w+ a+

newfile = open("./resources/newfile.txt", "w+")
newfile.write("\nsomething else")
newfile.seek(0)
print(newfile.read())
newfile.close()

#file closing with method
print(newfile.closed)
with open("./resources/newfile.txt", 'w') as f:
    f.write("Hello Python!!")
