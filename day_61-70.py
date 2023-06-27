## 61 - Inheritance in python
'''
When a class derives from another class. it can have its own properties and methods,this is called as inheritance.
Types of inheritance:

    Single inheritance
    Multiple inheritance
    Multilevel inheritance
    Hierarchical Inheritance
    Hybrid Inheritance
syntax ->
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
'''

# class Pro:
#     def __init__(self,name: str):
#         self.name=name

#     def pro_st(self):
#         print(f"This is Pro class and name->{self.name}")

# class Adv(Pro):         #inheritated pro class
#     def adv_st(self):
#         print(f"This is Adv class and name->{self.name}")

# obj1=Pro("cool")
# obj1.pro_st()
# # obj1.adv_st #will give error, we are accessing adv statement from pro class
# obj2=Adv("asd")     #we accessed pro class constructor in adv class 
# obj2.adv_st()


## 62  Access Specifiers/Modifiers
'''
    Public access modifier -> All the variables and methods (member functions) in python are by default public
    Private access modifier -> prefix its name with a double underscore (__)Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.
            Name mangling in Python is a technique to access private variable, we can access private attributes by calling _MyClass__"attribute_name"
    Protected access modifier ->  a member is protected is to prefix its name with a single underscore (_).
    '''

# class Fruit:
#     def pubName(self,value:str):
#         self.name=value     #public variable
#         print(f"fruit name is {self.name}")
    
#     def proName(self,value:str):      
#         self.__word=value   #An indication of private variable
#         print(f"fruit name is {self.__word}")

#     def _proVar(self):  # protected method
#         return "haha protected string"

# obj=Fruit()
# obj.pubName("banana")   
# print(obj.name)     #we can accessed public variable outside of class
# obj.proName("apple")    #we assign private variable some value
# # print(obj.__word)     #give error cause we are accessing private variable so we have to use name mangling
# print(obj._Fruit__word)     # _Myclass_variablename
# print(obj._proVar())    # calling by object of Fruit class, print protected method return statement