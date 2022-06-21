class School():
    students=[]
    def __init__(self,capacity):
        self.capacity=capacity
    def add_student(self, student):
        if self.capacity==len(self.students):
            print("list is full")
        else:
            self.students.append(student)
            print('{} is added to the list'.format(student.name))
    def print_students(self):
        for i in self.students:
            print(i)

class Students:
    def __init__(self,name,age,gender):
      self.name=name
      self.age=age
      self.gender=gender
      
        
    def __str__(self):
        return "Student with name {} and gender {}".format(self.name,self.age)
        
    
        
    
school=School(2)
student1=Students("John",23,"male")
student2=Students("Rambo",28,"male")
student3=Students("Camilla",19,"female")
school.add_student(student1)
school.add_student(student2)
school.print_students()
school.add_student(student3)
print(student1.__dict__)
