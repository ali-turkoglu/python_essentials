# for loop create an iter() automaticly. we can also create 

liste=[1,2,3,4,5,6]

iterator=iter(liste)
print(iterator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))



# for loop logic
while True: 
    try:
        element= next(iterator)
        print(element)
    except StopIteration:
        break    

##########################

class MyNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start<=self.stop:
            x=self.start
            self.start +=1
            return x
        else:
            raise StopIteration    

list=MyNumbers(11,22)            

for each in list:
    print(each)

