myDict = {
    "fast" : "in a quick manner",
    "kartik" : "future data scientist",
    "anotherdict" : {"sana" : "data scientist"}
}

# print(myDict['anotherdict']['sana'])
# print(myDict['kartik'])

# print(myDict.keys())
# print(myDict.values())
print(myDict.items())

updateDict = {
    "anshuman" : "friend",
    "aarushi" : "friend" , 
    "kartik" : "a dancer"
}

myDict.update(updateDict)
print(myDict)

print(myDict.get("kartik"))
print(myDict['kartik'])