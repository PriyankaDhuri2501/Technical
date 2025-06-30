#create student class takes marks of 3 sub as arguments in constructor and print the method to get average


class Student:
    def __init__(self,name,sub):
        self.name=name
        self.sub=sub
    def average(self):
        total = sum(self.sub.values())
        average=total/len(self.sub)
        print(self.name,"your Average is:",average)

sub={
    "Science": 50,
    "Maths":40,
    "English":30
}

name = str(input("Enter Your name "))
s= Student(name,sub)
s.average()
