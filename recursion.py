# --> Recursion : 
# -> When a function calls itself repeatedly. 
# -> We need 2 thing to work with Recursion 
#     -> Base Case.
#     -> Work you want to do.

# print n to 1 backwards:  
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("end")

# show(5)

# Factorial of a number using recursion :

# n = int(input("Enter the Number: "))
# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(n))

# Write a Recursive function to calculate the sum of Ist n natural number.
# def sumNaturalNumber(n):
#     if (n == 0) :
#         return 0 
#     else:
#         return n + sumNaturalNumber(n-1)

# print(sumNaturalNumber(5))

# Write a recursive function to print all the elements of a list.

# lst = [10, 20, 30, 40, 50]
# def print_list(lst):
#     if not lst:          
#         return
#     print(lst[0])        
#     print_list(lst[1:])  

# print_list(lst)

# ele = [10, 20, 30, 40, 50]
# def print_list(lst, index = 0):
#     if index == len(lst):
#         return
#     print(lst[index])
#     print_list(lst, index + 1)

# print_list(ele)

