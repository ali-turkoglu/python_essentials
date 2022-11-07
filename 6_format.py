name = "Kader"
lastName="Elnur"
age=35

print("my name is {}".format(name))
print("my name is {} {}".format(name,lastName))
print("my name is {n} {l}".format(n=name,l=lastName))
print("my name is {l} {n}".format(n=name,l=lastName))

print("my name is {} {} and I am {} years old".format(name,lastName,age))
print(f"my name is {name} {lastName} and I am {age} years old")


result=23/32
print("the result is {r:1.3}".format(r=result)) # 0.718
