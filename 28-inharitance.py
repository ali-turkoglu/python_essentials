# inharitance(Kalıtım): Miras alma

class Person():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print("person created")

    def who_am_I(self):
        print("I am "+self.firstname+" "+self.lastname)    


class Student(Person):
    
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber=number
        print("Student object created")

    #override
    def who_am_I(self):
        print("I am a student")    
    


class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname) # if we use super() into constructor, no need to pass self keyword
        self.branch=branch
        print("teacher created")


p1 = Person("Michael","Ericson")
s1 = Student("Daniel","Ervin",232)

p1.who_am_I()
s1.who_am_I()

t1=Teacher("Soner","Aru","Math")
