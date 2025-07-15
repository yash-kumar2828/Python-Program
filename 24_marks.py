marks1=int(input("enter marks1="))
marks2=int(input("enter marks2="))
marks3=int(input("enter marks3="))
total_per=(marks1+marks2+marks3)/3
if(total_per>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are pass:",total_per)
else:
    print("you failled, try again next year,",total_per)