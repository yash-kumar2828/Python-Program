# while loop 
i=1
while i<10:
    print(i)
    i=i+1

l=[1,"yash","kalpana",True,"yash kalpana"]
i=0
while i<len(l):
    print(l[i])
    i=i+1




# for loop with list
i=[1,2,3,4,5,6,8,7,6,5,4]
for item in i:
    print(item)

#for loop with iterate
for i in range(0,11,2):
    print(i)

#for loop with tuple
t=(1,2,3,2,1,45)
for i in t:
    print(i)
print(type(t))

#for loop with string
n="yash"
for i in n:
    print(i)


#for loop with else

i=[1,1,2,3,4,3,2]
for item in i:
    print(item)
else:
    print("done")


# break statement
for i in range(100):
    print(i)
    if i==10:
        break

#continue statement
for i in range(100):
    if i==10:
        continue
    print(i)

# pass statement
i=[1,2,3,4,5,6,7,10,122]
for item in i:
    # print(i)
    pass


for i in range(100):
    print(i)
    if i==10:
        break