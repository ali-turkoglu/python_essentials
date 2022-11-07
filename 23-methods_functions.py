#belongs to a class

str="Wooden Spoon"
list=str.split(" ")
print(list)

# to create a functin we use def keyword (define)
# we can call a functions directly without class or objects

def sayHello():
    print("Hello")

sayHello()    
sayHello()    
sayHello()   

def sayHello2(name):
    print("Hello " + name)
sayHello2("Dairly")    

def sayHello3(name):
    return "Hello "+name
str2=sayHello3("Willy")    
print(str2)

def total(num1,num2):
    '''
    DOCSTRING:Add two number
    INPUT: 2 int
    OUTPUT: 1 int
    '''
    return num1+num2
result=total(4,6)  
print(result)  
print(help(total))  # help