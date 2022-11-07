numbers=[1,2,3,4,5,6,7]

for each in numbers: 
    print(each)
    print("Hello")

names="David Harvest"
for n in names:
    print(n)

tuple=[(1,2),(1,3),(2,4)]  
for a,b in tuple:
    print(a,b)  

d={"key1":"value1","key2":"value2"}
for each in d:
    print(each)    #  keys

for each in d.items():
    print(each)    #  keys and values like ('key1', 'value1')

for x,y in d.items():
    print(x,y)    #  keys and values like key1 value1
    
for x,y in d.items():
    print(x)    #  keys 

for x,y in d.items():
    print(y)    #  values
    