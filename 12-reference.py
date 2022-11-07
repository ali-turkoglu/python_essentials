from tkinter import Y


x=12
y=23

x=y
y=56
print(x,y)

a=["apple","banana"]
b=["apple","banana"]

a=b

b[0]="grape"
print(a,b)  # as a=b a[0] also changed from apple to grape with b[0]