import os
# question number 1 if the word twinkle is present in the file or not
f = open('poems.txt')
t = f.read()

if 'twinkle' in t:
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()

# question number 2

# def game():
#     return 44656

# score = game()
# with open('hiscore.txt') as f:
#     hiscorestr = f.read()
# if hiscorestr == '':
#     with open('hiscore.txt', 'w') as f:
#         f.write(str(score))

# if int(hiscorestr)<score :
#     with open('hiscore.txt', 'w') as f:
#         f.write(str(score))

# question number 3

# for i in range(2,21):
#     with open(f"tables/multiplication_table_of_{i}", 'w') as f:
#         for j in range(1, 11):
#             f.write(f"{i}x{j}={i*j}")
#     break

#question number 4 a file contains a word multiple times and u have to censor that word from the file

# with open("donkey.txt", "r") as f:
#     content = f.read()

# content = content.replace("donkey", "#$@$#$@#")

# with open("donkey.txt", "w") as f:
#     f.write(content)

# question number 5 repeat question 4 with a list of words

# words = ["donkey", "dhechu", "word"]
# with open("donkey.txt", "r") as f:
#     content = f.read()
# for word in words:
#     content = content.replace(word, "#$@$#$@#")

# with open("donkey.txt", "w") as f:
#     f.write(content)

# question number 6 to find if "python" word is present in the log file or not

# with open("log.txt", "r") as f:
#     content = f.read()

# if 'python' in content.lower():
#     print("yes python is present")
# else:
#     print("python is not present")

# question number 7 to find in which line number "python" word is present

# content = True
# i=1
# with open("log.txt") as f:
#     while content:

#         content = f.readline()

#         if 'python' in content.lower():
#             print(content)
#             print(f"yes python is present on line number {i}")
#         i+=1

# question number 8 make a copy of a text file

# with open("this.txt") as f:
#     content = f.read()

# with open("copy.txt", "w") as f:
#     f.write(content)

# question number 9 to find if 2 files contents matches or not

# file1 = "copy.txt"
# file2 = "log.txt"

# with open(file1) as f:
#     f1 = f.read()

# with open(file2) as f:
#     f2 = f.read()

# if f1 == f2:
#     print("files are identical")
# else:
#     print("files are not identical")

# question number 10 to wipe out the contents of a file

# with open("copy.txt", "w") as f:
#     f.write("")

# question number 11 program to rename a file

# oldname = "copy.txt"
# newname = "renamed_by_python_copy.txt"

# with open(oldname) as f:
#     content = f.read()

# with open(newname, "w") as f:
#     f.write(content)

# os.remove(oldname)