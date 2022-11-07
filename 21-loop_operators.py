
# range() -> from starting point to stopping point  

for each in range(10):
    print(each)

for each in range(3,12):
    print(each)    

for each in range(0,100,10): #10-20-30-....90
    print(each)


# enumerate()   --> iterate no
str="Hello"
for each in enumerate(str):
    print(each) 
    #(0, 'H')
    #(1, 'e')
    #(2, 'l')
    #(3, 'l')
    #(4, 'o')

for x,y in enumerate(str):
    print(f"index no:{x} and letter: {y}")
    #index no:0 and letter: H
    #index no:1 and letter: e
    #index no:2 and letter: l
    #index no:3 and letter: l
    #index no:4 and letter: o


# zip() -->     join the lists
name=["ali","michael","jenett","donald"]
phone=[21323,23435,577654,345234]
age=[33,55,23,54]

list=list(zip(name,phone,age))
print(list)

for a,b,c in list:
    print(a,b,c)
