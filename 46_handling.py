try:
    a=int(input("enter a number:"))
    print(a)


except ValueError as v:
    print('hey')
    print(v)

except Exception as e:
    print(e)

print("thank you")