## 61 - Inheritance in python
'''
When a class derives from another class. it can have its own properties and methods,this is called as inheritance.
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


## 62