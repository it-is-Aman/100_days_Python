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



## 52 lambda function
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



## 53 Map, Filter and Reduce
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



## 54  'is' vs '==' in Python
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



## 55
# Snake Water Gun Exercise
'''
computer          S W G
                  0 1 2                 | column1 column2 column3
user        S 0   D W L         row1 ->
            W 1   L D W         row2 ->
            G 2   W L D         row3 ->

L=-1 D=0 W=1
'''
# Method 1
# import random
# def genereate_input():      #Each time you call the generate_input function, it will return a random value of either 0, 1, or 2.
#     return random.randint(0,2)

# def check(mat,val1,val2):
#     return mat[val1][val2]

# inputComp=genereate_input()
# inputUser=int(input("Enter 0-snake   1-water   2-gun:"))

# matrix=[[0,1,-1],        #matrix[1][2]=-1   2nd row and 3rd element
#         [-1,0,1],        #row=user, column=comp   
#         [1,-1,0]]

# result=check(matrix,inputUser,inputComp)
# if result==1:
#     print("|Won| \nyou choose:",inputUser,"computer choose:",inputComp)
# if result==-1:
#     print("|Lose| \nyou choose:",inputUser,"computer choose:",inputComp)
# if result==0:
#     print("|Draw| \nyou choose:",inputUser,"computer choose:",inputComp)


# Method 2
# import random
# def genereate_input():      #Each time you call the generate_input function, it will return a random value of either 0, 1, or 2.
#     option=['S','W','G']
#     return random.choices(option)

# def check(mat,val1,val2):
#     return mat[val1][val2]

# inputComp=genereate_input()
# inputUser=input("Enter S-snake   W-water   G-gun:")
# valUser=0 if inputUser=='S' else 1 if inputUser=='W'   else 2 
# valComp=0 if inputComp==['S'] else 1 if inputComp==['W']   else 2       #result is in terms of list so put in list format ['S'] when checking condition in "if" case 

# matrix=[[0,1,-1],        #matrix[1][2]=-1   2nd row and 3rd element
#         [-1,0,1],        #row=user, column=comp   
#         [1,-1,0]]

# result=check(matrix,valUser,valComp)
# if result==1:
#     print("|Won| \nyou choose:",inputUser,"computer choose:",inputComp)
# if result==-1:
#     print("|Lose| \nyou choose:",inputUser,"computer choose:",inputComp)
# if result==0:
#     print("|Draw| \nyou choose:",inputUser,"computer choose:",inputComp)



## 56 Introduction to OOP
'''
OOP in Python allows developers to model real-world concepts and entities using classes and objects, 
encapsulate data, reuse code through inheritance, and write more flexible code through polymorphism. 
'''


## 57
#  Python Class and objects
'''
# A class is a blueprint or a template for creating objects, providing initial values for state 
# (member variables or attributes), and implementations of behavior (member functions or methods).
# '''
# class UserDetails:
#     name="None"
#     roll=00

#     def info(self):  #self means that object for which this method is called
#         print(f"{self.name} is : {self.roll}")

# #Object is the instance of the class used to access the properties of the class Now lets create an object of the class.
# obj1=UserDetails()
# obj2=UserDetails()

# print(obj1.name)
# obj1.info()     

# obj2.name="cool"    #now name changed from default to "cool" in obj2
# obj2.roll=77
# obj2.info()     #info of obj2 will print and name,roll will be of obj2 because self method is called by object obj2



## 58
# Constructors
'''
A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. 
Constructor is invoked automatically when an object of a class is created.
syntax ->
def __init__(self):
	# initializations

1. Parameterized Constructor -> When the constructor accepts arguments along with self,
These arguments can be used inside the class to assign the values to the data member

2. Default Constructor -> When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor
'''
#Default Constructor
# class student:
#     def __init__(self):     #called automatically when an object is created of a class
#         print("this is the constructor")

#     name="None"
#     mark="00"

#     def details(self):
#         print(f"{self.name} obtained {self.mark}")

# a=student()
# a.name="cool"
# a.mark=23
# a.details()


#Parameterized Constructor

# class student():
#     def __init__(self, name,mark):  #self is must to have   
#         self.stuName=name       #(keep in mind) the syntax, 'name' is like a local parameter but 'stuName' is class variable so, use stuName whenever use in class.
#         self.stuMark=mark

#     def details(self):
#         print(f"{self.stuName} obtained {self.stuMark}")    #keep in mind syntax

# #b=student("cool")    #give error because required arguments are missing
# b = student("cool",77)    
# b.details()



## 59 Python Decorators
'''
Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and method
python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code
'''

# def greet(fx):  #take its own function, here 'fx' name could be any
#     def mfx():      #modified function, here 'mfx' name could be any
#         print("Welcome")    #print 1st message
#         fx()        #print the content of that function
#         print("End")        #print last message
#     return mfx      #return our this fully modified function

# @greet      
# def hello():        #function will print with that greet funciton everytime whenever we call this function
#     print("this is just a hello function")

# hello()

# # greet(hello)()      #shorthand use



## 60 Getters and Setters
'''that's why we use getter,setter,deleter
# print(fruit_obj.fruit_name)     #we are refering fruit_name as local variable even thought this is a getter variable

Getters -> typically defined using the @property decorator,
           getters do not take any parameters.

Setters-> setters take self, value as parameters,
          we need setter method which can be added by decorating method with @property_name.setter
'''

# method 1

# class Fruit:    
#     def __init__(self,name: str):       #this only take string
#         self._name=name         #underscore syntax for creating private variable (_name)

#     def get_name(self):     #here we get the name of our fruit
#         print("getting name")
#         return self._name
        
#     def set_name(self,new_name: str):       #here we set the new_name of our fruit into our private variable
#         self._name=new_name

# fruit_obj=Fruit("banana")
# # print(fruit_obj._name)      #we can still access _name which should be private
# fruit_obj.set_name("orange")        #we set the name from banana to orange
# print(fruit_obj.get_name())     #we get orange instead of banana beacuse we were set that

# method 2

# class Fruit:
#     def __init__(self,name: str):
#         self._name=name

#     @property       #what ever we write under this will gonna be consider as property and it acts as a getter
#     def fruit_name(self):
#         print(f"{self._name} was accessed")
#         return self._name
    
#     @fruit_name.setter      #we use our property with setter,deleter and @property_name should be same as @property
#     def fruit_name(self,value):     #setter should have self and value 
#         print(f"{self._name} is now {value}")
#         self._name=value        #we are setting our self._name "original class variable" to new value

#     @fruit_name.deleter      
#     def fruit_name(self):     
#         print(f"{self._name} was delected")
#         del self._name    #delete our self._name value

    
# fruit_obj=Fruit("banana")
# print(fruit_obj.fruit_name)     #we are refering fruit_name as local variable even thought this is a getter variable
# fruit_obj.fruit_name="orange"   #here we have triggered setter method 
# del fruit_obj.fruit_name    #which will delete the attribute means "orange"