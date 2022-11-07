a,b,c,d= 5,5,10,4

result=(a==b) #True

result=(a==c) #False

result=(a!=c) #True
result=(a>c) #False
result=(a<c) #True
result=(a<=b) #True

result=(True==1) #True

result= True+40 #41

#-------------------------------------------

a=int(input("enter a number: "))
b=int(input("enter a number: "))

if(a>b):
    print(f"{a} number is bigger than {b} ")
else:
    print(f"{a} number is smaller than {b}")

