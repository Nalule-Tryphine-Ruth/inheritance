class Student:
    def __init__(self,regno,name,age):
           self.regno = regno
           self.name = name
           self.age = age
           
    def Study(self):
               return "I am studying"
    def Play(self):
               return "I am playing"
    def Discuss(self):
              return "I am Discussing"
    def __str__(self):
        return f"I am {self.name} my RegNo is {self.regno} and am {self.age} years"
    
    
          
          
student1=Student("J22B13/049","Tryphine",20)
print(student1)
print(student1.Study())




class NetworkAdmin(Student):
       def __init__(self):
            

