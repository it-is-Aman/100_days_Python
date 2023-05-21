# # import module
# import flask


# print("Awesome")

# # \" -> if wants to print " in sentence
# print("This is the reference of \"basic sentence\"")                                        


## 5
# #comments 
# '''this is 
# the example of 
# multiple comments'''

# #sep = seperate the objects " " by default , end = what to print at end "\n" by default
# print("wow",7,'haha')
# print("wow",7,'haha',sep="-",end="99")


## 6
# #type
# a=2
# b="wow"
# print(type(a))
# print(type(b))


## 7
## exercise 1 -> calculator
# a=5
# b=3
# print("addition",a+b)
# print("subtraction",a-b)
# print("multiplication",a*b)
# print("exponential",a**b)
# print("division",a/b)
# print("Modulus",a%b)
# print("Floor division",a//b)


## 9
# #typecasting
# a="2"
# b="4"
# c=2.2
# d=4

# print(a + b)    #print 24
# #explicit typecasting
# print(int(a) + int(b))  #print 6
# #implicit typecasting
# print(c+d)  #print 6.2 this change d into float


## 10
# #input
# a=int(input("enter your number"))
# print("your number is", a)


## 11
# #string
# str='''this is 
# multiple string'''
# print(str)

# #prints 2nd str word
# print(str[1])

# #prints word using for loop
# for word in str:
#     print(word)


## 12
# #string slicing
# str="Awesome"
# # print(str)
# # print(str[0:])  #print till end
# # print(str[0:5]) #including 0 but not 5

# print(str[0:-3])    #python automatically add len() whenever -ve comes
# print(str[0:len(str)-3])    #same as above 

# if "ame" in "name":
    # print("yes")
# else:
    # print("no")

## 13
# #string methods -> Strings are immutable
# str="aweSOMe BUddy , this is GOing to Big  !!!!"

# print(str.upper())
# print(str.isupper())    
# print(str.lower())
# print(str.islower())    #True if all the characters in the string are lower case
# print(str.swapcase())   #changes the character casing of the string. Upper case are converted to lower case and lower case to upper case
# print(str.replace("BUddy","Man"))
# print(str.endswith("this"))    
# print(str.startswith("this"))    
# print(str.capitalize()) #turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase
# print(str.title())  #capitalizes each letter of the word within the string.
# print(str.istitle())    #True only if the first letter of each word of the string is capitalized,
# print(str.count("this"))    #returns the number of times the given value has occurred
# print(str.find("this")) #searches for the first occurrence of the given value    
# print(str.index("this")) #searches for the first occurrence of the given value, raise an exception if not present    
# print(str.strip())  #removes any white spaces before and after the string.
# print(str.rstrip("!"))  #removes any trailing characters
# print(str.split())   ##Splits the string at the whitespace " "
# print(str.center(100,"."))  #string to the center as per the parameters given by the user, will print "." in every feild
# print(str.isalnum())    #true only if the entire string only consists of A-Z, a-z, 0-9
# print(str.isalpha())    #true only if the entire string only consists of A-Z, a-z
# print(str.isprintable())    # True if all the values within the given string are printable,  if "\n" then return False
# print(str.isspace())    #True only and only if the string contains white spaces


## 14
# #if - elif - else ladder
# a=int(input("enter your number: "))
# if(a>0):
#     print("number is positive")
# elif(a<0):
#     print("number is negetive")
# else:
#     print("number is zero")


## 15
## Exercise 2 -> Good Morning Message
# from time import strftime   #keep in mind use from ___ import ____
# if(int(strftime("%H"))>6 and (int(strftime("%H"))<12)):
#     print("GOOD MORNING")
# else:
#     print("SLEEP")

#     #OR
# import time 
# if(int(time.strftime("%H"))>6 and (int(time.strftime("%H"))<12)):
#     print("GOOD MORNING")
# else:
#     print("SLEEP")


## 16
## match case -> break statement aren't here, in match case only one case will execute

# x=23
# match x:
#     case 0:
#         print("x is 0")
#     case 5:
#         print("x is 5")
#     #default case only match if above case were not matched and also if condition matched but next default condition not execute
#     case _ if x!=20:
#         print("default x is not 20")
#     #default case only match if above case were not matched
#     case _:
#         print("default")


## 17
## for loop

# str="meow"
# for i in str:
#     # print(i,end=",")
#     print(i)

# for num in range(10):   #print 0 to 9
#     print(num)

# for num in range(1, 10):    #print 1 to 9   
#     print(num)

# for num in range(1, 10, 2):    #print 1 to 9 with omitted 2 place values   
#     print(num)


## 18
## while loop

# num=1
# while(num<10):
#     print(num)
#     num=num+1

#emulate do-while loop -> use infinite while loop with break statement in an if statement that check condition and break iteration if condition becomes true
# while True: 
#     num=int(input("enter num: "))
#     print(num)
#     if  num<0:   #or if not num>0
#         break


## 19
## continue and break

# for i in range(1,20):
    # if i==14:
    #     print("break moves out of the loop")
    #     break
    # if i==11:
    #     print("continue skips the iteration")
    #     continue
    # print(i)


## 20
## functions

# def area(r):
#     return 3.14*r**2
# def circum(r):
#     print("circumference is: ",2*3.14*r)
# def volume(r):
#     pass    #this will simply pass this function and interpreter go to next line

# radius = 3
# print("area of circle: ",area(radius))
# circum(radius)


## 21
## function arguments

# #default argument
# def num(a=2, b=3):
#     print("a =",a,"b =",b)

# num()
# num(5)  #only a changes to 5
# num(b=7)    #b chanes to 7 but a is 2

# #keyword argument ->  order in which the arguments are passed does not matter.
# def num(a=2, b=3):
#     print("a =",a,"b =",b)

# num(b=7, a=0)

# # Required argument -> necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.
# def num(a, b):
#     print("a =",a,"b =",b)

# # num(4)  #give error
# num(4,7)

##Variable-length arguments
    ##arbitrary -> The function accesses the arguments by processing them in the form of tuple
# def num(*num):
#     print(num[0],num[1],num[2])
# num(2,5,7)    

    ##keyword arbitrary -> The function accesses the arguments by processing them in the form of dictionary.
# def name(**name):
#     print(name["name1"],name["name2"])
# name(name1="wow",name2="nice")    



## 22
## list -> Lists are changeable

# list = [1,2,3,4,5,6,7]
# name = [23,"wow","noice",77]
# # print(list)
# # print(name)

# print(name[0])
# print(name[1])
# print(name[-2]) #same as print(name[len(name)-2])

## Check whether an item in present in the list?. This is done using the in keyword.
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Green" in colors:
    # print("Green is present.")
# else:
#     print("Green is absent.")

# if "ame" in "name":
    # print("yes")
# else:
    # print("no")

## range of index -> listName[start : end : jumpIndex]
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes
# print(animals[-7:-2])	#using negative indexes'
# print(animals[1:6:2])	#using positive indexes every 2rd consecutive value 

##List Comprehension
# '''Syntax:
# List = [Expression(item) for item in iterable if Condition]
# Expression: It is the item which is being iterated.
# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# Condition: Condition checks if the item should be added to the new list or not.
# '''
# num=[1,2,3,4,5,6]

# lst=[i**2 for i in range(11)]   #with this help element(i) become part of list
# print(lst)

# list=[i**2 for i in num if i%2==0]  #keep in mind (syntax)
# print(list) #add i**2 expression in list only when if condition is true


## 23
## List methods -> he original list is updated

# l=[1,5,4,9,10,6,3,6]
# print(l)

# l.sort()    #sorts the list in ascending order. The original list is updated
# # l.sort(reverse=True)    #print the list in descending order
# # l.reverse() #reverses the order of the list.
# # l.append(9) #This method appends items to the end of the existing list.
# # l.insert(3,77)  #This method inserts an item at the given index. insert item(77) at index 3
# # print(l.index(5))   #returns the index of the first occurrence of the list item.
# # print(l.count(6))   #Returns the count of the number of items with the given value.

# # #this method of copy is not good for beginner because it also modifies original list
# # m=l
# # m[0]=55
# # print(l)    #list l is also modified
# # print(m)

# # m=l.copy()  #Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
# # print(m)

# # m=[77,88,99]
# # k=l+m   #You can simply concatenate two lists to join two lists
# # print(k)

# # m=[77,88,99]
# # l.extend(m) #This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list. list of m elements added to the end of list l. but changes are done in original list l
# # print(l)

# print(l)


## 24
## Tuples -> tuple items are seperated by comma, enclosed with (), unchangeable

# tup=(1,)    #in tuple comma is necessory otherwise python take it as int datatype
# print(type(tup),tup)    

# tup=(1,5,4,2,3)
# tup.sort()  #we can't use because tuple are immutable
# print(tup)

# tup = (1,2,3,4,"wow")
# # tup[1]=4    #can't because tuple can't be modified
# print(type(tup),tup)
# print(tup[1])
# print(tup[-2])
# print(tup[0:])
# print(tup[1:3])
# print(tup[0:5:2])
# if 2 in tup:
#     print("present")
# tup2=tup[1:3]   #new tuple will create
# print(tup2)


## 25
## Operations on tuples

'''manipulating Tuple
if you want to add, remove or change tuple items, then first you must convert the tuple to a list.
Then perform operation on that list and convert it back to tuple.
'''


# tup=("wow",4,2,6,"asd")
# temp=list(tup)
# temp.append(99)
# temp.pop(2) #pop element at index 2
# temp[1]=11
# tup=tuple(temp)
# print(tup)

# tup1=("qwerty","wow")
# tup2=(1,2,3,4,5)
# tup3=tup1 + tup2    #we can directly concatenate two tuples without converting them to list.
# print(tup3)

# # Tuple methods
# tup=("wow",4,2,6,4,"asd")
# # n=tup.count(4)    #The count() method of Tuple returns the number of times the given element appears in the tuple.
# # n=tup.index(4)  #This method raises a ValueError if the element is not found in the tuple.
# n=tup.index(4,2,5)  #returns the first occurrence of the given element from the tuple from index 2 to 4 (5 not included).

# print(n)


## 26 exercise 2 solution already done in #15
## 27
## exercise 3 -> kaun banega carorpati

# que=["question 1","question 2","question 3","question 4","question 5","question 6"]
# ans=["answer 1","answer 2","answer 3","answer 4","answer 5","answer 6"]
# i=0
# price=0

# while(True):
#     print(que[i])
#     value=input("enter your answer\n")
#     if(value==ans[i]):
#         i=i+1
#         price=price+1
#     else:
#         print("you lose")
#         break

# print("total answers",i,"your price is",price)


## 28
## f string -> f""

# str="Man your name is {} and ID no is {}"
# name="cool"
# num=14588
# print(str.format(name,num)) #this will replace first {} with name means cool and 2nd {} with num means 14588

# name="wow"
# num=789
# str=f"Name is {name} and ID no is {num} and its {{workflow}}"   #we can put all valid Python expressions in them. {{}} if you want to show single {} in print message
# print(str)

# money=1099.999999
# str=f"mrp of new item is {money:.2f}"   #print upto 2 decimal places money value
# print(str)


## 29
''' Docstrings in python -> are the string literals that appear right after the definition of a function, method, class, or module.
We can access these docstrings using the doc attribute __doc__
'''


# def sum(a,b):
#     #wow    #simple comment interpreter will ignore
#     # w=3   #if w=3 in function then dostring could not print
#     '''This function will return sum of 2 variable'''  #this docstring only with ''' ''' 
#     return a+b

# s=sum(2,4)
# print(sum.__doc__)  #this print docstring which wrote in between ''' '''
# print(s)


## 30
## Recursion

# #factorial
# def fac(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fac(n-1)
# n=5
# print("factorial of",n,"is",fac(n))

# #fibonacci
# def fib(n):
#     if n==0:
#         return n
#     elif n==1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)    #f0=0   f1=1 so, f3=f0+f1 means f(n)=f(n-1)+f(n-2)
# n=5
# print("fibonacci of",n,"is",fib(n))


## 31
## Set -> they cannot be accessed using index numbers.
'''Sets are unordered collection of data items. They store multiple items in a single variable.
Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable,
meaning you cannot change items of the set once created. Sets do not contain duplicate items.
'''


# s={"bill",112,"location",78.8,112}
# print(s)    #print unorderly, not duplicate, cannot be accessed using index numbers.

# s=set()     #empty set
# print(type(s))

# #access set items
# s={"bill",112,"location",78.8,112}
# for item in s:
#     print(item)


## 32
## Set Methods
## Joining Sets

# set1={1,5,4,2,6,3}
# set2={5,1,8,9,6,2}

# # union() and update() -> prints all items that are present in the two sets.
# print(set1.union(set2)) #union() method returns a new set
# # # set1.update(set2) #update() method adds item into the existing set from another set.
# print(set1)

# # intersection and intersection_update() -> prints only items that are similar to both the sets.
# # print(set1.intersection(set2))
# # # set1.intersection_update(set2)
# # print(set1)

# # symmetric_difference and symmetric_difference_update() -> prints only items that are not similar to both the sets.
# # print(set1.symmetric_difference(set2))
# # # set1.symmetric_difference_update(set2)
# # print(set1)

# # difference() and difference_update() -> prints only items that are only present in the original set and not in both the sets.
# # print(set1.difference(set2))
# # set1.difference_update(set2)
# # print(set1)


##Set Methods

# set1={1,2,3,4,5,7}
# set2={2,4,7}

# # print(set1.isdisjoint(set2))    # checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
# # print(set1.issuperset(set2))    #checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
# # print(set2.issubset(set1))  #checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

# # print(set1.add(9))  #add a single item to the set 
# # print(set1)

# # set1.update(set2)   #add more than one item,use update() method to add it into the existing set.
# # print(set1)

# # set1.remove(2)  #remove item from set, if we try to delete an item which is not present in set, then remove() raises an error
# # print(set1)

# # set1.discard(9)  #remove item from set, if we try to delete an item which is not present in set, then discard() does not raises an error
# # print(set1)

# # val=set1.pop()  #removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
# # print(set1)
# # print(val)

# # set1.clear()    #clears all items in the set and prints an empty set.
# # print(set1)

# # del set1    #keyword which deletes the set entirely.
# # print(set1) #raise error because set1 has been deleted

# if 7 in set1: #You can also check if an item exists in the set or not.
#     print("present")
# else:
#     print("not")


## 33
## Dictionaries -> Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

# info = {
#     "name":"awesome",
#     "roll":7,
#      "id":333,
# }

# print(info) #print our dictionary

# # print(info["name"]) #access dict. value by mentioning key in [], if not found so it will give error
# # print(info.get("name")) #access value by mentioning key by using get method, if not found so will give None

# # print(info.keys())  #print all the keys in the dictionary using keys() method.
# # print(info.values())    #print all the values in the dictionary using values() method

# # print(info.items()) #print all the key-value pairs in the dictionary using items() method. 

# for k,v in info.items():    #Respected Dictionary keys and values goes into k and v from info.items(), k and v created tuple
#     print(f"keys is {k} and resp. values is {v}")

# # for key in info.keys(): #for printing values with help of keys in f string
# #     print(f"key is {key} and resp. value is {info.get(key)}")


## 34
## Dictionary Methods

# val1 = {1:11 , 2:22 , 3:33 , 4:44 , 5:55}
# val2 = {8:88 , 9:99}

# # val1.update(val2)   #same like union in sets, updates the value of the key provided to it if the item already exists in the dictionary.
# val1.update( {6:66} ) #updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair
# print(val1)

# # val1.clear()    #Removes all the items from the list.
# # print(val1)

# val1.pop(5)  #removes the key-value pair whose key is passed as a parameter.
# print(val1)

# # val1.popitem()  #emoves the last key-value pair from the dictionary.
# # print(val1)

# del val2[8] #if key is provided it delete the key-value pair 
# # del val2    #If key is not provided, then the del keyword will delete the dictionary entirely.
# print(val2)


## 35
## for Loop with else in Python ->
'''
The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
'''


# for i in range(10):
#         print (i)

# else:
#     print("else statement") #will print because break statement is not used in for loop


# # for i in range(10):
# #         print (i)
# #         if i == 5:
# #             break

# # else:
# #     print("else statement") #will not print because break statement used in for loop


## 36
## Exception Handling
'''
try….. except blocks are used in python to handle errors and exceptions.
The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.
try:
     #statements which could generate 
     #exception
except:
     #Soloution of generated exception
'''


# try:
#     val = int(input("enter your value:"))
#     print(f"your num is {val}")
# except Exception as e:  #this will show the exception and print message in e accordingly
#     print(e)

# print("End of programm")    #this will print even if our program contain error because we used exception handling

# # try:
# #     val = int(input("enter your value:"))
# #     print(f"your num is {val}")
# # except ValueError: #we can use many exception according to respective error
# #     print("Value error")
# # except IndexError:  
# #     print("Index error")


## 37
## Finally  Keyword
'''''
The finally block is always executed, so it is generally used for doing the concluding 
tasks like closing file resources or closing database connection or may be ending the 
program execution with a delightful message

try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation
'''


# def func():
#     try:
#         l=[1,2,3,4]
#         val=int(input("enter your index:"))
#         print(l[val])
#         return 1

#     except:
#         print("Error occured")
#         return 0

#     finally:
#         print("Finally always executed irrespective of their position") #this will print even if we returned any value in function

# num=func()
# print(num)


## 38
## Custom Error -> In python, we can raise custom errors by using the raise keyword. sometimes we may need to create our own custom exceptions that serve our purpose.

# num = int(input("enter num between 3 and 8:"))
# print(f"your num is {num}")

# if (num<3 or num>8):
#     raise ValueError("Value error")  #it will print ValueError: Value error


## 39
## Exercise 3 -> (KBC) solution, but i made a quize game

# # use dictionery with list in it and answer always at index 0 which will be changed in sorted value
# Questions = {
#     "How many cm in 1 m":[100,90,10,1000],  
#     "How many pieces in 1 dorzen":[12,6,18,20],
#     "How many metre in 1 km":[1000,100,10,10000],
# }

# for que,ans in Questions.items():
#     print(f"{que} ?")
#     correct_answer=ans[0]

#     #this will sort the key's and store in sorted_opt
#     sorted_opt= sorted(ans) 
#     # print(sorted_opt) #use just for printing the sorted list

#     #enumerate() to print the index of each answer alternative: use i+1 so, give user flexibility to choose and print sorted option
#     for i,opt in enumerate(sorted_opt):
#         print(f"{i+1}->{opt}")

#     #user value goes into user_option and then check through sorted_opt index's      'sorted_opt[user_option-1]' 
#     #then assign into user_answer
#     '''
#     little explanation
#     ans[0]=100       sorted_opt[] 0th   10         user_option=3       sorted_opt[user_option-1] = 100         so, answer is correct
#                                   1st   90
#                                   2nd  100
#                                   3rd 1000
#     '''
#     user_option=int(input("choose from 1 - 4 : \n"))    
#     user_answer=sorted_opt[user_option-1]

#     #if correct_answer which is unsorted key's 1st value == user_answer from checked through sorted option   then print success 
#     if user_answer == correct_answer:
#         print("congratutions")
#     else:
#         print(f"you lose correct answer is {correct_answer!r} not {user_answer!r}") #!r written answer in between ''
#         break


## 40
## Exercise 4: Secret Code Language -> my simple programm
'''
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
'''


# import string

# def encrypt(word):
#     if len(word)<=3:
#         encrypt_word = word[::-1]   #[::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.

#     else:
#         ran="tyr"
#         f_word=word[0]
#         word=word[1:] 
#         #s_word=word.split()    #Not used but, It then joins all but the last word back together using the join method and slicing the list from the beginning to the second-to-last element. Finally, the function returns the resulting string.
#         word=word+f_word
#         encrypt_word=ran+word+ran

#     return encrypt_word

# def decrypt(word):
#     if len(word)<=3:
#         decrypt_word = word[::-1]   #[::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.

#     else:
#         word=word[3:len(word)-3]
#         # l_word=decrypt_word[len(decrypt_word)]    #ChatGPT solve this problem
#         l_word=word[-1]
#         # decrypt_word[len(decrypt_word)]=''  #gives error ChatGPT Corrected me
#         decrypt_word=l_word+word[:-1]

#     return decrypt_word

# # def decrypt(word):    #ChatGPT given this function yeah, which worked fine
# #     if len(word) <= 3:
# #         return word[::-1]

# #     decrypt_word = word[3:len(word)-3]
# #     last = decrypt_word[-1]
# #     decrypt_word = last + decrypt_word[:-1]

# #     return decrypt_word

# user_word=input("enter your message: ")

# print(f"user word {user_word}")

# encrypted_word=encrypt(user_word)
# print(f"user encrypted word: {encrypted_word}")

# decrypted_word=decrypt(encrypted_word)
# print(f"user decrypted word: {decrypted_word}")

# print("Thanks for using this encryptor")






