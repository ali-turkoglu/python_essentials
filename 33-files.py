# we use open() function to open a file
#open(fileName,openTextMode)
                # w write -> if there is a info in the file, it clears old info and writes new info 
                # a append
                # x create
                # r read
                # r+ read and write

# files should close with close() function

file = open("33-newFile.txt","w",encoding="utf-8")
file.write("Ali Tamtamış")
file.close()   

file2 = open("C:/Users/alitu/OneDrive/Desktop/33-newfile2.txt","w")
print(file2)
file2.close()


# a -> with a mode we can add new info end of the info, it does not delete old info
file3=open("33-newfile3.txt","a",encoding="utf-8")
file3.write("\nDeneme deneme")
file3.close()

# x it just create a file, if file is exist, it will throw error

# if we do not pass a mode parameter, default is r(read)
file=open("33-newfile3.txt",encoding="utf-8")
for i in file:
    print(i,end="") # print function throw a empty line after printing. avoid empty line we can add end=""
file.close()  

# read() instead for loop
file=open("33-newfile3.txt",encoding="utf-8")
print("\niçerik 1")
content1=file.read(5)
print(content1)
content1=file.read(4)
print(content1)
content1=file.read(7)
print(content1)
content1=file.read()

print(content1)
file.close()

# readline() -> it reads one line each time
file=open("33-newfile3.txt",encoding="utf-8")
print(file.readline())
print(file.readline())
print(file.readline())

# readlines()
file=open("33-newfile3.txt",encoding="utf-8")
liste=file.readlines()
print(liste)

# using with 
with open("33-newfile3.txt",encoding="utf-8") as file:
    content=file.read()
    print(content)
    # no need to use file.close()

# tell -> to learn the location of cursor 

# seek() -> to send the cursor specific location 
# seek(0) -> cursor goes to the top of the file


  

try:
    file=open("newfile44.txt")
except FileNotFoundError:
    print("file read error") 
finally:
    file.close()    















