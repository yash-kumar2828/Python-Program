# wap to store seven fruts in a list entered  by the user 
fruits=[]
f1=input("enter fruits name:")
fruits.append(f1)
f2=input("enter fruits name:")
fruits.append(f2)
f3=input("enter fruits name:")
fruits.append(f3)
f4=input("enter fruits name:")
fruits.append(f4)
f5=input("enter fruits name:")
fruits.append(f5)
f6=input("enter fruits name:")
fruits.append(f6)
f7=input("enter fruits name:")
fruits.append(f7)
print(fruits)





# wap to accept marks of 6 students and display them in a sorted manner
marks=[]
f1=int(input("enter marks name:"))
marks.append(f1)
f2=int(input("enter marks name:"))
marks.append(f2)
f3=int(input("enter marks name:"))
marks.append(f3)
f4=int(input("enter marks name:"))
marks.append(f4)
f5=int(input("enter marks name:"))
marks.append(f5)
f6=int(input("enter marks name:"))
marks.append(f6)
marks.sort()
print(marks)


# check that a type cannot be changed in python 
a=(20,"yash")
a[1]="Kumar"
print(a)

# wap to sum a list with 4 numbers 
l=[70,80,30,10]
print(sum(l))



# wap to count the number of zeros in the following tuple 
a=(7,0,8,0,0,9)
no=a.count(0)
print(no)