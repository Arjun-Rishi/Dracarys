class Employee:
    def __init__(self,name,age,position):
        self.name=name
        self.age=age
        self.position=position

    def salary(self,salary):
        self.salary=salary
        return salary
        
teacher=Employee("Swathi",23,"English Teacher")
print("Name: ",teacher.name)
print("Age: ",teacher.age)
print("Working as: ",teacher.position)
print("Salary: ",teacher.salary(10000))