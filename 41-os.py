#info about operating system
import os 
import datetime

result=dir(os)

result=os.name

#changing directory
#os.chdir("c:\\")
# os.chdir("..")
# os.chdir("../..")


#creating dir
# os.mkdir("deneme")
# os.makedirs("deneme/newdirectory")


#rename dir
#os.rename("deneme","test")

#os.rmdir("test")
#os.removedirs("test/newdirectory")


#listeleme
# result= os.listdir()
# result= os.listdir("c:\\")
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)


# working directory
result=os.getcwd()


result= os.stat("40-date_time.py")
#result=result.st_size/1024
result1 = datetime.datetime.fromtimestamp(result.st_atime)   #creating time
result1= datetime.datetime.fromtimestamp(result.st_ctime)   #last accessing time
result1 = datetime.datetime.fromtimestamp(result.st_mtime)   #modify time

os.system("calc.exe")

#path
result= os.path.abspath("41-os.py")
result=os.path.dirname("C:/Users/alitu/ideaprojects/python_essentials/41-os.py")

result=os.path.dirname(os.path.abspath("41-os.py"))

result=os.path.exists("41-os.py")  # True

'''
os.path.
        isdir()
        isfile()
        join()
        split()
        splitext()

'''


print(result1)