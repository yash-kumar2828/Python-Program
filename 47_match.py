def http(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return 'not found'
        case 500:
            return "internal server error"
        case _:
            return "unknown status"

print(http(501))



dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
merged=dict1 | dict2
print(merged)