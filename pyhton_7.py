# a = []
# for i in range(1, 6):
#     a.append(i * 2)
# print(a)    

# Converting into List Comprehension

# a = [i * 2 for i in range(1,6)]
# print(a)

# a = []
# for i in range(1,50):
#     if i % 7 == 0:
#         a.append(i)
# print(a)
 
# a = [i for i in range(1,50) if  i % 7 == 0]
# print(a)

# a = [num if num<5 else num * 2 for num in range(2,9)]
# print(a)

# a = []
# for num in range(2, 9):
#     if num<5:
#         a.append(num)
#     else:
#         a.append(num*2)
# print(a)

# lst = [33, 63, 22, 15, 9, 88, 77]
# a = [i for i in lst if i % 3 == 0]
# print(a)

# lst = [("a", 11), ("b", 12), ("c", 13)]
# new_lst = [n * 3 for (x,n) in lst if x == "b" or x == "c"]
# print(new_lst)

# result = []
# for x in [10,5,2]:
#     for y in [2,4,3]:
#         result.append(x ** y)
# print(result)

# result = [x**y for x in [10,5,2] for y in [2,3,4]]
# print(result)

