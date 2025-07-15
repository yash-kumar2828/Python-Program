class employee:
    name="yash"
    age=20

emp1=employee()
print(emp1.name,emp1.age)



# instance vs class 
class employee:
    company="google"
emp1=employee()
emp1.name="yash"
emp1.sal="40k"
print(emp1.company,emp1.name,emp1.sal)
employee.company="youtube"
print(employee.company)
employee.company="yash"
print(employee.company)




# self parameter
class employee:
    lan="python"
    salary=40000
    def getInfo(self):
        print(f"THE LANGUAGE IS {self.lan}.the salary is {self.salary}")
    def greet(self):
        print("good morning")
emp1=employee()
emp1.getInfo()
emp1.greet()


# static method

class employee:
    lan="python"
    salary=40000
    def getInfo(self):
        print(f"THE LANGUAGE IS {self.lan}.the salary is {self.salary}")
    @staticmethod
    def greet():
        print("good morning")
emp1=employee()
emp1.getInfo()
emp1.greet()


# constructor
class employee:
    lan="python"
    salary=40000
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print("i am creating an object")
    def getInfo(self):
       print(f"THE LANGUAGE IS {self.lan}.the salary is {self.salary}")
    @staticmethod
    def greet():
        print("good morning")
emp1=employee("yash",60000)
emp1.getInfo()
print(emp1.name,emp1.salary)
emp1.greet()


