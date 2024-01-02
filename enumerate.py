list1 = [3, 54, 34, False, 5.6, "Kartik"]

# index = 0
# for item in list1:
#     print(item, index)
#     index += 1

# instead of using this we can use enumerate function mentioned below
for index, item in enumerate(list1):
    print(item, index)