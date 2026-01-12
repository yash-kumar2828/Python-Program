# example of dictionary
marks={
    "yash":100,
    "kumar":95
}
print(marks)
print(type(marks))
print(marks["kumar"])


# dictionary method
a={
    "name":"yash",
    "from":"India",
    "marks":[98,89,87,78,95]
}

print(a.items())
print(a.keys())
print(a.values())

a.update({"from":"Bihar"})
print(a)

print(a.get("marks"))

a.pop("name")
print(a)

a.popitem()
print(a)

