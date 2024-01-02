# a = {1,2,3,4,5,3,2,1}

# print(type(a))

# print(a)

a = set()
a.add(3)
print(a)
print(type(a))

a.add(4)
a.add(10)
a.add((3,8,9))
# a.add({4:5})
print(a)

# print(len(a))
a.remove((3,8,9))
print(a)

b = len(a)

print(b)

print(a.clear())
print(a)

