# we use decorators to add a feature into the functions

def my_decorator(func):
    def wrapper(name):
        print("before function")
        func(name)
        print("after function")
    return wrapper

def sayHello(name):
    print("Hello ",name)

@my_decorator
def sayGreeting(name):
    print("Greeting ",name)    

sayGreeting("Ahmet")  

###################################
import math
import time

def calculate_time(func):
    def inner(*args,**kvargs):
        start=time.time()        
        time.sleep(1)
        func(*args,**kvargs)
        finish=time.time()
        print(func.__name__+" takes "+ str(finish-start)+" seconds.")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)   

usalma(4,2)     







