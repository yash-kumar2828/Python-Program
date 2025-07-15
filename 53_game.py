import random
n=random.randint(1,100)
a=-1
guess=0
while a!=n:
    guess+=1
    a=int(input("guess the number:"))
    if a>n:
        print("lower number please:")
    else:
        print("higher number please")
print(f"you have guessed the number {n} currectly in {guess} attempts")