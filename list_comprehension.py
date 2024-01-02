#to find all the even numbers in a and print it in a new list that is b
a = [3, 6, 7, 8, 9, 2, 34, 23, 123, 56]
# b = []
# for item in a:
#     if item%2==0:
#         b.append(item)

# print(b)
#now to shorten it out we can do the below statement
b = [i for i in a if i%2==0]
print(b)

t = [1,4,3,4,1,2,3]
s = {i for i in t}

print(s)