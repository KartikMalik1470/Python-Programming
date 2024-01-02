# # 
# def is_monotonic(arr):
#     inc = True
#     dec = True

#     for i in range(1, len(arr)):
#         if arr[i] > arr[i-1]:
#             dec = False
#         elif arr[i] < arr[i-1]:
#             inc = False
#     return inc or dec

# '''while True:
#     try:
#         input_str = input("Enter elements of the array separated by spaces: ")
#         arr = [int(num) for num in input_str.split()]
#         break  # Exit the loop if input is successfully processed
#     except ValueError:
#         print("Invalid input. Please enter integers separated by spaces.")

# # Continue with the rest of your code here
# print("Array:", arr)'''   
# while True:
#     try:
#         a1 = input("enter elements of the array with spaces: ")
#         arr = [int(num) for num in a1.split()]
#         break #exit if input is success

#     except ValueError:
#         print("invalid input, please enter the elements with a space in between")

# # arr = [6,5,4,3,2,1]

# if is_monotonic(arr):
#     print("the array is monotonic")
# else:
#     print("the array is not monotonic")

word = "kartik "

letters = [i for i in word]

letter_sorted = sorted()

print(type(letters))
print(letters)