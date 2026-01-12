# example of set
s=set()
s.add(1)
s.add(2)
s.add(3)
s.add(10)
s.add(8)
print(s)
print(type(s))
set={10,10,5,5,20,20,"yash"}
print(set)
print(type(set))


# list method
s={"yash",1,2,1,2,10,5,"kumar"}
print(s)
s.add(190)
print(s)

print(len(s))

s.remove("yash")
print(s)

s.pop()
print(s)

s.clear()
print(s)

s2=s.union({10,29,5,1,2,60,"kumar"})
print(s2)


s2=s.intersection({1,2,10,20,"yash"})
print(s2)