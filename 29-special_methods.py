# there are many special methods to use in our class. but we have to override into new class

list=[1,2,3]

class Movie():
    def __init__(self,filmName,duration):
        self.filmName=filmName
        self.duration=duration
        print("movie object created")

    # to use special object that was created for all classes like print,len etc.
    # we have to overide that special methods

    def __len__(self):
        return self.duration

    def __del__(self):
        print("movie object deleted") 




m=Movie("Harry Potter",120)
print(m.filmName,m.duration)

print(len(m))
