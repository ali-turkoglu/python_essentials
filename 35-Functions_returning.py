def usalmaTaban(number):
    def usalmaUst(power):
        return number**power
    return usalmaUst    

print(usalmaTaban(2)(3))
#or
two=usalmaTaban(2)
print(two(3))       # 2**3

three=usalmaTaban(3)
print(three(3))     # 3**3


print("################################")

def counting(countName):
    def add(*args):
        add=0
        for i in args:
            add+=i
        return add

    def multiply(*args):
        multiply=1
        for i in args:
            multiply*=i
        return multiply
    if countName=="add":
        return add
    elif countName=="multiply":
        return multiply
    else:
        print("wrong type")

add=counting("add")
multiply=counting("multiply")

print(add(2,5,7,8))
print(multiply(4,6,8))

