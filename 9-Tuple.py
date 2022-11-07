# we can not change elements in tuple after assigne but we can reassigne

list=[1,2,3]

tuple=(1,2,"three",False)
tuple= 1,2,"three",False

print(tuple[2]) #three

print(len(tuple))

names=("Omer","Deniz") + tuple

print(names)
