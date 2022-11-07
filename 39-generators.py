#bellek üzerinde yer tutmayan bir iterator şekli

# iterator ile kullanım, burada liste memory de yer tutar. list sonra kullanılabilir
def cube():
    list=[]
    for each in range(5):
        list.append(each**3)
    return list

print(cube())    

# eger sadece bir kere print için bu iterator yapılıyorsa generator kullanılabilir. memory de yer tutmaz ama sonra da kullanılamaz

def cube2():
    for each in range(5,10):
        yield each **3   # return yerine yield keyword kullanırız

print(cube2())

generator = cube2()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

####################################

list1 = [i**3 for i in range(5)]  # iterator

list2 = (i**3 for i in range(5))  # generator

print(list1)
print(next(list2))
print(next(list2))
for i in list2:
    print(i)