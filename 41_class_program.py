class program:
    company="microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=program("yash",1200000,844111)
print(p.name,p.salary,p.pin)


# calaculator
class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube(self):
        print(f"the square is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"the square is {self.n**1/2}")
    @staticmethod
    def hello():
        print("yash kumar")
a=calculator(4)
a.square()
a.cube()
a.squareroot()
a.hello()



class demo:
    a=4
o=demo()
print(o.a)
o.a=0
print(o.a)
print(demo.a)


from random import randint
class train:
    def __init__(self,trainno):
        self.trainno=trainno
    def book(self,fro,to):
        print(f"ticket is booked in train no: {self.trainno} from {fro} to {to}")
    def status(self):
        print(f" train no: {self.trainno} is running on time")

    def fare(self,fro,to):
        print(f"ticket fare  in train no: {self.trainno} from {fro} to {to} is {randint(222,5555)}")
    

t=train(12007)
t.book("patna","delhi")
t.status()
t.fare("patna","delhi")




        

