# wap  using function to convert celcius to faherenheit
def f_to_c(f):
    return 5*(f-32)/9
f=int(input("enter temprarture i f="))
print(f_to_c(f))


# wap function which converts inches to cms.
def i_t_c(inch):
    return inch*2.54
n=int(input("enter value in inches="))
print(f"the corresponding value in cms is= {i_t_c(n)}")