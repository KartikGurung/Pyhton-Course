# Map Function : It executes a specified fucntion for each items in a iterable. The item is sent to function as a parameter.

# ages = [5, 12, 13, 14, 18, 90, 67, 56]
# def myfun(x):
#     if x<18:
#         return False
#     else:
#         return True
    
# def myfun_1(x):
#     return x * x

# adult = list(filter(myfun, ages))

# for x in adult:
#   print(x)

# square = map(myfun_1, adult)

# for x in square:
#     print(x)

# With Lambda : 
 
# ages = [5, 12, 13, 14, 18, 90, 67, 56]

# adult = list(filter(lambda x : x>=18, ages))

# square = list(map(lambda x : x * x, adult))
# for x in square:
#     print(x)

