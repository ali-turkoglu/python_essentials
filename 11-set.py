# in set list there is no index

fruits={"orange","apple","banana"}

for x in fruits:
    print(x)

fruits.add("cherry")

print("----------------------------")

for x in fruits:
    print(x)

print("--------------------------------")

fruits.update(["mango","pepper"])

for x in fruits:
    print(x)

fruits.remove("apple")
fruits.discard("banana")    
fruits.clear()