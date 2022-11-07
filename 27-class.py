import datetime

class Person:
    # pass  # pass keyword can be used for avoiding error if there is no statement in class or function etc.

    #class attributes
    address="no info"

    #constructor
    def __init__(self,name,year,job):      # self=this in java , we can use this
        self.name=name
        self.year=year
        self.job=job
        print("__init__ method run") # this constructor method run for every created object

    #methods  
    def intro(self):    # put self to call this method through the object
        print("Hello "+self.name) 

    def calculateAge(self):
        return 2022-self.year  
          

#object(instance)
p1 = Person("David",1990,"student")


#updating
p1.address="ankara"


#accessing object attributes
print(p1.name,p1.year,p1.job)
print(p1.name,p1.address)

p1.intro()
print(p1.calculateAge())

