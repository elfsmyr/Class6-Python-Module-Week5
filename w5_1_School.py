class School():
    students=[]
    capacity=2

class Students(School):
    def __init__(self):
      self.name=''
      self.age=int
      self.gender=str
      
        
    def __str__():
        print()
        
    def add_student(self):
        if self.capacity==len(self.students):
            print("list is full")
        else:
            self.students.append(self.name)
            print('{} is added to the list'.format(self.name))
        
    def print_students():
        for i in School.students:
            print(i)
school=Students()
student1=Students()
student1.name='John'
student1.age=23
student1.gender='male'
student2=Students()
student2.name='Rambo'
student2.age=28
student2.gender='male'
student3=Students()
student3.name='Camilla'
student3.age=19
student3.gender='female'
Students.add_student(student1)
Students.add_student(student2)
Students.print_students()
Students.add_student(student3)
print(student1.__dict__)
