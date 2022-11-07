#insert students info given from user in a dictionary 

students={}

number=input("student no: ")
name=input("student name: ")
phone=input("student phone no: ")

""" students[number]={
    "name":name,
    "phone":phone
    }
     """
    
students.update({
    number:{
        "name":name,
        "phone":phone
    }
})

number=input("student no: ")
name=input("student name: ")
phone=input("student phone no: ")
students.update({
    number:{
        "name":name,
        "phone":phone
    }
})

print(students)

studentNo= input("enter student no: ")
print(students[studentNo])
