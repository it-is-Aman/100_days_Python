## List Comprehension
#name = [1,2,3,4,5,6]
# nameList=[ i*10 for i in name if (i<5)]
# print(nameList)

## List methods
# l=[1,2,3,4,5]
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
