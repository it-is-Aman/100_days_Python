## 51  seek() and tell() functions
'''
the seek() and tell() functions are used to work with file objects and their positions within a file
seek() - allows you to move the current position within a file to a specific point.
tell() - returns the current position within the file, in bytes. 
'''

# with open("file_io.txt","r") as file:
#     file.seek(3)    # Move to the 3th byte in the file
#     text = file.read(4)     # Read the next 4 byte
#     print(text)
#     print("current position",file.tell())   #return the current position

# with open("file_io.txt","a") as file:
#     file.write("this is from seek() and tell() function")    # Move to the 3th byte in the file
#     file.truncate(26)   #if you want to truncate the file to a specific size, it only print upto 26 byte and only write 'this i' because previous string char also come in 26 byte

# with open("file_io.txt","r") as file:
#     print(file.read())


## 53 lambda function
'''
a lambda function is a small anonymous function without a name.
lambda arguments: expression
'''

# def add(num1,num2):   # Function to add the input
#     return num1+num2
# print(add(2,3))

# add = lambda num1,num2: num1+num2   # Lambda function to add the input
# print(add(1,3))

# def add_adt(fx , num):      #fx have anonymous function which do square of the number
#     return num + fx(num)    # 5 + 5**2 = 5 + 25 = 30

# print(add_adt(lambda num: num**2,5))    #we created anonymos function and pass to function


## 54 Map, Filter and Reduce
'''
the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence.
These functions are known as higher-order functions, as they take other functions as arguments.
map(function, iterable) - The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
filter(predicate, iterable) - The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate.
reduce(function, iterable) - The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python.
'''

# map
# def square(num):
#     return num**2
# l=[1,2,3,4]      # List of numbers
# print(l)
# new_l=map(square,l)     #square each number using the map function
# print(list(new_l))      # Print the doubled numbers

# l=[1,2,3,4]      # List of numbers
# print(l)
# new_l=map(lambda num:num**2,l)     #The map function applies the lambda function to each element in the list
# print(list(new_l))      # list containing the doubled numbers


#filter
# def even(num):
#     return num%2==0
# l=[1,2,3,4]      # List of numbers
# print(l)
# new_l=filter(even,l)     # Get only the even numbers using the filter function
# print(list(new_l))      # Print the even numbers

# l=[1,2,3,4]      # List of numbers
# print(l)
# new_l=filter(lambda num:num%2==0,l)     #The filter function applies the lambda function to each element in the list
# print(list(new_l))      #new list containing only the even numbers


#reduce
# from functools import reduce

# # def sum(num1,num2):
# #     return num1+num2
# # l=[1,2,3,4]      # List of numbers
# # print(l)
# # new_l=reduce(sum,l)     # Calculate the sum of the numbers using the reduce function
# # print(new_l)      # Print sum       1+2,3,4 = 3+3,4 = 6+4 = 10  

# l=[1,2,3,4]      # List of numbers
# print(l)
# new_l=reduce(lambda num1,num2:num1+num2,l)     #lambda function to the first two elements in the list (1 and 2), then applies the function to the result (3) and the next element (3), and so on.
# print(new_l)      #the sum of all the elements in the list



## 55  'is' vs '==' in Python
'''
while the == operator compares the values of the objects. This means that is will only return True if the objects being compared are the exact same object in memory,
while == will return True if the objects have the same value.
'''

# obj_a=3     #strings and integers are immutable means their value can't be changed so both result will be same
# obj_b=3
# print(obj_a is obj_b)
# print(obj_a == obj_b)

# obj_a=[1,2]     #list and dictionaries are mutable so is and == behave differently
# obj_b=[1,2]
# print(obj_a is obj_b)
# print(obj_a == obj_b)

# obj_a=(1,2)     #tuple are immutable means their value can't be changed so both result will be same
# obj_b=(1,2)
# print(obj_a is obj_b)
# print(obj_a == obj_b)





























