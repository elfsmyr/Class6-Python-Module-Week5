class Rectangle:
    def __init__(self,length,width):
          self.length=length
          self.width=width
     
    def  perimeter(self):
        return 2*(self.width+self.length)
    
    def area(self):
        return self.width*self.length
        
    def display(self):
      print("width : ",self.width)
      print("lenght : ",self.length)
      print("perimeter : ",self.perimeter())
      print("area : ",self.area())
p1=Rectangle(5,20)
p1.display()

class Parallelepipede(Rectangle):
    def __init__(self, length, width,height):
        self.height=height
        super().__init__(length, width)
        
    def volume(self):
        print(self.width*self.height*self.length)
p1=Parallelepipede(5,20,3)
p1.volume() 