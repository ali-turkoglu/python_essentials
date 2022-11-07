#creating custom exception

# x=10

# if x>5:
#     raise Exception("x can not be more than 5")


def check_password(psw):
    import re # regular expressions
    if len(psw)<8:
        raise Exception("password can not be less than 8 characters")
    elif not re.search("[a-z]",psw):
        raise Exception("password should include at least 1 small letter") 
    elif not re.search("[A-Z]",psw):
        raise Exception("password should include at least 1 capital letter")
    elif not re.search("[0-9]",psw):
        raise Exception("password should include at least 1 number")           
    elif not re.search("[_@$]",psw):
        raise Exception("password should include at least 1 alpha numeric character") 
    elif re.search("\s",psw):
        raise Exception("password should not include space") 
    else:
        print("valid password")    



while True:
    password=input("enter a password: " )
    try:
        check_password(password)
    except Exception as ex:
        print(ex)
    else:
        print("valid password")
        break
    finally:
        print("finally block")         


class Person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception("name should be less than 10 characters")  
        else:
            self.name=name          

p=Person("Alilllllllllllllll",1999)
        