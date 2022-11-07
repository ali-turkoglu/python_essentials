# we can not change value type with functions
def changeName(n):
    n="Ali"
name="Ahmet"
changeName(name)
print(name)     #Ahmet

# we can change referance type with functions. more than 1 referance for 1 list
def changeListElement(n):
    n[0]="Istanbul"
list=["Ankara","Izmir"]
changeListElement(list)
print(list)     #['Istanbul', 'Izmir']


# functions with 2, 3 or more arguments
def add1(a,b,c=0):
    return sum((a,b,c))

def add2(a,b,c=0,d=0):
    return sum((a,b,c))

def add3(*params):
    return sum(params) #we can pass arguments how many we want with * (tuple lists)

print(add1(4,6))
print(add1(4,6,7))   
print(add3(1,4,6,2,3,6,8,3,23,9)) 

def displayUser(**args): # we can pass dictionary type params/args with ** (dictionary=map in java)
    for key, value in args.items():
        print(f"{key} is {value}")

displayUser(name="Çınar",age=23,city="ankara",email="cinar@gmail.com")

def myfunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)



