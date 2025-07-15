# write a recursive functon calculate the sum of n natural numbers
def sum(n):
    if n==1:
        return 1
    return sum(n-1)+n
print(sum(5))

def pattern(n):
    if n==0:
        return
    print("*"*n)
    pattern(n-1)
pattern(10)


