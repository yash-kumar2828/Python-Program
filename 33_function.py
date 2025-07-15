def add(*args):
    sum=0
    for i in args:
        sum+=int(i)
    return sum
res=add(10,20)
print(res)
res=add(10,101,10)
print(res)


# function definition
def avg():
    a=int(input("enter a number="))
    b=int(input("enter a number="))
    c=int(input("enter a number="))
    average=(a+b+c)/3
    print(average)

# function call 
avg()
add()


