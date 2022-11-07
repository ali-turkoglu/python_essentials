# Exceptions 

# print(a) -> NameError

# int("1h2") -> ValueError

# print(10/0) -> ZeroDivisionError

# print("denem"e) -> SyntaxError

###############################################

# try:
#     x = int(input("x= "))
#     y = int(input("y= "))
#     print(x/y)
# except Exception as e:
#     print("invalid entry: ",e)

while True:
    try:
        x = int(input("x= "))
        y = int(input("y= "))
        print(x/y)
    except Exception as e:
        print("invalid entry, please try again: ",e)
    else:
        break 
    finally:
        print("there is a try except blok") 


            





