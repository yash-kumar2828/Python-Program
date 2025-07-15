import math
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

num=int(input("enter a number="))
if prime(num):
    print(num,"is prime number")
else:
    print(num,"is not prime number")

