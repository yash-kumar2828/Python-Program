# wap to find the greats of four numbers entered by the user 
n1=int(input("enter first number="))
n2=int(input("enter second number="))
n3=int(input("enter third number="))
n4=int(input("enter fourth number="))
if(n1>=n2 and n1>=n3 and n1>=n4):
    print("greatest number is n1:",n1)
elif(n2>=n1 and n2>=n3 and n2>=n4):
    print("greatest number is n2:",n2)
elif(n3>=n1 and n3>=n2 and n3>=n4):
    print("greatest number is n3:",n1)
else:
    print("greatest number is n4:",n4)   
