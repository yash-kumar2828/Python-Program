
name="yash"
nameshort=len(name)
print(nameshort)

name1="yash kumar"
namesort1=name[0:8]
print(namesort1)
print(name1[-8:-1])
print(name1[0:])

word="principle"
newword=word[1:6:2]
print(newword) 

str="yash"
mystring=str.endswith("sh")
print(mystring)
 
str1="yash"
mystring1=str1.startswith("ya")
print(mystring1)


name2="yash"
capital=name2.capitalize()
print(capital)


a="yash singh"
index=a.find("singh")
print(index)

a1="yash kumar"
replaced=a1.replace("kumar","singh")
print(replaced)

# escape sequence characters
a="yash is a good boy \nbut not a bad  \"boy\""
print(a)