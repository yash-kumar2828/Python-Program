# wap to print multiplication table of a given number using for loop 
num=int(input("enter a number="))
for i in range(1,11):
    table=num*i
    print(f"{num} * {i}={table}")


# while loop 
n=int(input("enter a number="))
i=1
while(i<11):
      print(f"{n} * {i}={n*i}")
      i=i+1