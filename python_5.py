# List : A built in data type that stores an ordered collection of items inside a single variable. 
# we can store different data types in a list.

#list["20", 20, 1]
#list[0] = "10"
#print(list)

#-------------------------------------------------------------------------------#

#list slicing : list [startidx:endidx:jump]
#my_list=[20, 20, 1, 22, 33, 88]
#print(my_list[1:len(my_list)])

#-------------------------------------------------------------------------------#

# Listing Method : 
# 1. Append List(adding of an element in a List)
#my_list=[2,1,4,6]
#my_list.append(8)
#print(my_list)

# 2. Sort List(Sort the element in the List)
#my_list=[2,1,4,6]
#my_list=["banana", "kiwi", "apple"]
#my_list.sort()
#print(my_list)

#letter  = ["b", "h", "k", "l"]
#letter.sort(reverse = True)
#letter.reverse()
#print(letter)

# 3. Insert List : Insertion of an element in the list
#my_list=[0,0,0,20,20]
#my_list.insert(3,0)
#print(my_list)

# 4. Remove List : Remove an element from the list
#my_list=[0,0,0,20,20] 
#my_list=[0,0,0,20,0,20]
#my_list.remove(20) #we can remove the element from the list using the element i.e. 20.
#print(my_list)

# 5. Pop List : Pop the element from the List.
#my_list=[0,0,0,20,20] 
#my_list.pop(3) #we can pop out the element using the index number.
#print(my_list)


# Nested List : A list inside a list is called a nested List.
#a = [10, 20, 30, [20,30]]
# indexing in nested list : 0, 1, 2, (3,0, 3,1)
#a = [10, 20, 30, [20,30]]
# a[3][0] = 40
# a[1] = 100
# print(a)
# b = [10, 20, 30, [40, 50]]
# b[1] = 40
# b[3][1] = 60
# print(b) 

#----------------------------------------------------------#

# To do :
#append = "apple" --> Done
#reverse sort --> Done
#sort() --> Undone
#my_list=["banana", "True", 4, 55, "55", "666", 55] 
#my_list.append("apple")
#my_list.reverse()
#my_list.sort()
#print(my_list)

#To DO: 
# insert = 9th idx "Yaseen"
#remove --> yaseen
#pop(0th)

#my_list.insert(9, "Yaseen")
#my_list.remove("Yaseen")
#my_list.pop(0)
#print(my_list)

#my_list=["banana", "True", 4, 55, "55", "666", 55]
#for i in my_list :
#    print(i)
#i = 0
#while(i<len(my_list)):
#    print(my_list[i])
#    i += 1
#print(my_list)
#print(my_list[2:0:-1])

#-------------------------------------------------------------------------#

# Tuple : Built-in(or in-built) data type which is used to store multiple items in a single variable-. Kind of list but it is immuteable. 

#tuple = (8,9,0,1)
#print(tuple[0])

#tup = (1) # if a single element is present, the complier treat it as an integer.
#print(type(tup)) #--> output : type 'int'

#if 
#tup = (1, ) # Now the compiler treat this as a tuple beacuse it has more than one element present
#print(type(tup)) #--> output : type 'tuple'

#tup2 = (1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5)
#print(tup2.index(3)) #--> output : 2 because it shows index of that element that we are asking.
#print(tup2.count(5))

#----------------------------------------------------------------------------#

# Q: write a program if a list contains palindrome(a word, phrase, number or sequence that reads the exact same forwards and backwards) of elements.
# racecar.

#Method 1 : Using slicing

#lst = ["racecar"]
#for word in lst:
#    if word == word[::-1]:  # Here we used the concept of slicing to prove if the word is a palindrome or not.
#        print(word, "is a palindrome")
#    else:
#        print(word, "is not a palindrome")


# Method 2 : Using reverse function

# lst = list(input("Enter the word: "))
# reverse_lst = lst.copy()
# reverse_lst.reverse()

# if lst == reverse_lst:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Method 3 : Using list function and reverse function 

# n = input("Enter: ")
# rev = list(n)
# rev.reverse()
# if list(n) == rev:
#     print( n,"is a Palindrome")
# else:
#     print(n ,"is not a Palindrome")

#----------------------------------------------#

# str = "MIETClass"
# str.replace("MIET", "Miet")
# print(str.replace("MIET", "Miet"))

#-----------------------------------------------------------------------#

#Maximum  Element in a List :

# Q: WAP to find the Maximum element in a list.

# list=[10, 20, 80, 40, 50]
# #list = input("Enter the Elements: ")
# max = list[0]
# # Find Max element function :
# for i in list:
#     if i > max:
#         max = i

# print(max, "is the maximum element in the list")

#------------------------------------------------------------------------#

# Q: WAP to count the even number in a list.
# n = input("Enter the element: ")
# list = n.split()
# even_count = 0
# for i in list:
#     if (int(i)%2 == 0):
#         even_count += 1
    
# print("Even Number: ", even_count)

#--------------------------------------------------------------------------#

# Q: WAP to find the second largest element of a list 

# n = input("Enter the element: ") # --> lst = [60, -10, -50, -30, 0, 15]
# list = n.split()
# Second Largest Element Logic goes from here:
# n = len(list)  # --> Lenght of the list
# for i in range(0,n): # --> i traverse list form 0 to n
#     for j in range(i+1, n): # --> j traverse list from i+1 to n
#         if(list[i]>list[j]):  # --> Condition goes from here 
#             temp=list[i]
#             list[i]=list[j]
#             list[j]=temp
# print("Second Largest element in a list :",list[-2])
    

# Optimal Code :
# lst = [60, -10, -50, -30, 0, 15]        
# largest = second_largest = float('-inf')  # --> Chain assignment a = b = _?_?_

# for i in lst:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i != largest:
#         second_largest = i

# print("Second Largest element in the list is:", second_largest)

#-------------------------------------------------------------------------------------#