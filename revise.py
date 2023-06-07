##List
l=[1,2,3,4,5]
# m=l.copy()
# print(m)
# l.reverse()

## Tuple
# l=(1,2,3,4,5)
# l2=l
# print(l2)

## manipulating Tuple
# tup=[1,2,3,4,5]
# lst=list(tup)
# lst.append(69)
# lst.pop(3)
# lst.insert(1,7)
# print(lst)
# tup=tuple(lst)
# print(tup)

## f string -> f""
# userName = 'cool'
# userId = 7
# userSentence=f"your username is {userName} and allocated Id is {userId}"
# print(userSentence)

## docstrings
# def sumTwoNum(a,b):
#     '''this is docstring and function will print sum'''
#     return a+b
# print(sumTwoNum.__doc__)
# print(sumTwoNum(2,4))

## set
# setNum = {1,2,5,3,6,4,3,1,2,2,2,0}
# for num in setNum:
#     print(num,end=' ')

## set methods
# set1={1,3,5,6}
# set2={2,3,4,5}
# unionSet=set1.union(set2)   #union will be stored into unionSet
# print(unionSet)
# set1.update(set2)   #set1 have union of both set
# print(set1)
# set1.add(77)    #77 will add anywhere 'cause set is unordered
# print(set1)

## dictionary
# dic = {
#     "name":"awesome",
#     "roll":7,
#     "id":333,
# }
# print(dic)
# print(dic.items())
# for key in dic.keys():
#     print(f" {key} = {dic.get(key)}")

## Exception Handling
# try:
#     num=int(input("enter your number"))
#     print("your num is",num)
# except :
#     print('enter integer value')

# def sum():
#     try:
#         num1=int(input("enter num1"))
#         num2=int(input("enter num2"))
#         return num1+num2
#     except Exception as msg:
#         print(str(msg))
#     finally:
#         print("this will print whether error occur or not")
# print(sum())


## Custom Error
# num1=int(input("enter num1: "))
# num2=int(input("enter num2: "))
# sum=num1+num2
# if(sum>69):
#     raise ValueError("naughty boy your sum is greater than 69")
# else:
#     print(sum)


# str="aweSOMe BUddy , this is GOing to Big "

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
# print(str.isspace()) 


# lst=[1,2,3]
# print(lst)

# tup=(1,4,6,2,4,0)
# print(tup)
# tup=list(tup)
# tup.sort()
# print(tup)

# set={2,4,4,1,1,1,7,9}
# print(set)
# set.remove(4)
# print(set)

# dic={"fir":"lol",
#      "wer":"ppp",
#      "asd":"sam"}
# print(dic.items())
# print(dic.keys())
# print(dic.values())