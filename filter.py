# Filter in Python :
# filter():
# returns an iterator where the items are filtered through a function to test if the item is accepted or not. 

# ages = [3, 5, 6, 17, 18, 21, 24]
# def myfun(x):
#     if x < 18:
#         return False
#     else:
#         return True
# adults = list(filter(myfun, ages))
# for x in adults:
#     print(x)

# With Lambda and Filter :
# ages = [3, 5, 17, 18, 24]
# adults = list(filter(lambda n : n>=18, ages))
# for x in adults:
#     print(x)

# Find even values of a list using filter :
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def even(n):
#         if n % 2 == 0:
#             return True
#         else:
#             return False
# even_values = list(filter(even, lst))

# for n in even_values:
#     print(n)

# With Lambda
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_values = list(filter(lambda n : n % 2 == 0, lst))
# for n in even_values:
#     print(n)

