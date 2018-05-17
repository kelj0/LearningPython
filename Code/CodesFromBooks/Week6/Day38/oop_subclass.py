#!/usr/bin/python3
#!/usr/bin/python3
class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))
    
    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=" ")

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('(Initialized Teacher:  {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print("(Iniutialized Student: {})".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Zlatan',69,40000)
s = Student('Keljo',3000,99999)

print()

members= [t,s]
for members in members:
    members.tell()