class  Person:
    name=''
    age=''
    def display(self):
      print("name    :",self.name)
      print("age     :",self.age)
      
class Student(Person):
    section=''
    def display(self):
      print("name    :",self.name)
      print("age     :",self.age)
      print("section :",self.section)
      
      
student1=Student()
student1.name='elif'
student1.age='22'
student1.section='data science'
student1.display()

student2=Person()
student2.age='28'
student2.name='merve'
student2.section='data science'
student2.display()