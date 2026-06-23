# Pattern Printing :

# n = int(input("Enter the Number: "))
# for i in range(n):
#     for j in range(n): 
#         print("*", end=" ") 
#     print()

#--------------------------------------------#

# WAP to calculate the sum of positive numbers of a list.

# n = int(input("Enter the number: "))
# lst = n.split()
#  lst = [10, -20, 20, 30]
# sum = 0
# for i in lst:
#     if i>0:
#         sum += i
# print(sum)

#----------------------------------------------#

#WAP to find the missing number in a list

# lst = [1, 2, 4, 5]
# n = len(lst)+1
# # for i in range(1, n+1):
# #     if i not in lst:
# #         print(i, "is the missing number in the list")
# expected_sum = n * (n+1) // 2
# actual_sum = sum(lst)

# missing_number = expected_sum - actual_sum

# print(missing_number)

# lst=[-1, -2, -3, -4, -5, -7, -8, -9]
# for i in range(min(lst), max(lst)+1):
#     if i not in lst:
#         print("The missing number is:",i)

# n = int(input("Enter the number: ").strip())
# l = len(str(n))
# print(l)

# def isArmstrong(n):
#         num = n
#         sum = 0
#         while num > 0:
#                 digit = num%10
#                 sum += digit ** l
#                 num //= 10
#         return sum == n
        
# if isArmstrong(n):
#         print("Armstrong")
# else:
#         print("Not Armstrong")

