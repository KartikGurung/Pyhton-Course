# -> Lambda Function :
#     -> Also k/as as anonymous function.
#     -> Q : A lambda function can take multiple argument or not ?
#     -> A : It can take any number of arguments. But can only have one expression.
#     -> syntax :
#         -> lambda arg, expression.
    # ->
#-----------------------------------------------------------#

# print((lambda x : x ** 2)(5))
# x = lambda a,b,c : a+b+c
# print(x(5,6,2))

# Write a fucntion to calculate the sum of all natural number.

# def sumNaturalNumber(n):
#     if (n == 0) :
#         return 0 
#     else:
#         return n + sumNaturalNumber(n-1)

# print(sumNaturalNumber(5))

sum_n = (lambda n : n*(n+1)//2)
print(sum_n(5))

