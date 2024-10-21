# class firstcode:
from itertools import batched
from typing import override

#     a=10
#     b=20
    
 
#     def display(self,x):
#         print("Hello World!!", self.a + self.b + x )

#     def show(self):
#         result = self.display(5)
#         print(result)

# obj = firstcode()
# obj.display(25)
# obj.show()

# #################Constructor#####################################
# class firstcode:

#     a=10
#     b=20
    
#  #define with __init__
#  #self used to access all the properties from class
#  #no need to call , its auto executed
#     def __init__(self,xValue):
#         self.x = xValue
#         print( self.a + self.b + xValue )
#         print(self.x)

# ## a,b is a class variable
# ## xValue is a instance variable

# obj = firstcode(100)
# print(obj.x)




#################Static Property###################

# class firstcode:
#
#     a=10
#     b=20
# #in python do not need to  make variable static cz it can be accessed outside of the class without creating object by default
# #No need to create object
#     @staticmethod
#     def display():
#         z= firstcode.a + firstcode.b
#         print(z)
#
# firstcode.display()
# print(firstcode.a)
#
# #Accessing after creating object
# obj = firstcode()
# obj.display()
# print(obj.b)
#

##############Inheritence################
# # Example of Single Inheritance
# class Animal:
#     def speak(self):
#         return "Animal makes a sound."
#
# class Dog(Animal):
#     def speak(self):
#         return "Dog barks."
#
# # Example of Multiple Inheritance
# class Flyer:
#     def fly(self):
#         return "Can fly."
#
# class Bird(Animal, Flyer):
#     def speak(self):
#         return "Bird chirps."
#
# # Example of Multilevel Inheritance
# class Mammal(Animal):
#     def walk(self):
#         return "Mammal walks."
#
# class Cat(Mammal):
#     def speak(self):
#         return "Cat meows."
#
# # Testing Single Inheritance
# print("Single Inheritance:")
# dog = Dog()
# print(dog.speak())  # Output: Dog barks.
#
# # Testing Multiple Inheritance
# print("\nMultiple Inheritance:")
# bird = Bird()
# print(bird.speak())  # Output: Bird chirps.
# print(bird.fly())    # Output: Can fly.
#
# # Testing Multilevel Inheritance
# print("\nMultilevel Inheritance:")
# cat = Cat()
# print(cat.speak())  # Output: Cat meows.
# print(cat.walk())   # Output: Mammal walks.


########################################################################

# class father:
#
#     def __init__(self):
#         print("I am father")
#
# class son(father):
#
#     def __init__(self):
#         super().__init__()
#         print("I am Son")


#obj = son()
#obj1 = father()
# If Parent has static properties, child can access as it is like parent
# - If Child has static properties, Parent can't access as it is like child
# - How child can access parents static and non-static properties

################Methode Overriding########################


# class father:
#
#     x=20
#     y=30
#
#     def add(self):
#         print(self.y + self.x)
#
# class son(father):
#
#     def add(self):
#         print(self.y + self.x +30)
#
#
# obj = son()
# obj.add()


################## abstraction ########################
# #abc = abstract base class, its a library where all the abstraction properties are ramained
# from abc import ABC,abstractmethod
#
# class Bangladesh(ABC):
#     @abstractmethod
#     def print_num(self):
#         for i in range(11):
#             print(i)
#     @abstractmethod
#     def father_(self):
#         pass
#
# #child class must enforce or implement father class
# #No object can be created in abstracted class
# class Dhaka(Bangladesh):
#
#     def father_(self):
#         print("I am father")
#
#     def print_num(self):
#         for i in range(11):
#             print(i)
#
# obj = Dhaka()
# obj.print_num()
# obj.father_()

########### Methode Overloading #################

#same name different parametre
#in python its not like that

# *a = variable length argument, as many as parameter i can add
#use default parameter

# class father:
#
#     x=20
#     y=30
#
#     def add(self,a=0,b=0):
#         print(self.y + self.x +a+b)
#
#
#
# obj = father()
# obj.add(b=30)
# obj.add(20,30)


############## Access Modifier ################

# class father:
#
#     x="BMW"
#     _y="Toyota" #protected
#     __z="Ford"
#
#     def add(self):
#         print(f"Our brand name is {self.x}")
#
# class son(father):
#     def display(self):
#         print(self._y)
#
# #public(accessible from inside class , Outside class, child class)
# #protected(accessible from inside class , Outside class(not recommended), child class)
# #private(accessible from inside class , Outside class(No access), child class/subclass(no access)
#
#
# obj = father()
# print(obj.x)
# obj.add()
# obj1 = son()
# obj1.display()


############ Getter setter ##############

#used to access private variables

# class car:
#     __brand="Toyota"
#     __make = "2021"
#     @property
#     def display(self):
#         return f'"{self.__brand},{self.__make}"'
#
#     @display.setter
#     def display(self,values):
#         self.__brand,self.__make =values
#
# obj = car()
# obj.display = "Ford","2022"
# print(obj.display)

############### Encapsulation ###################
#used for data protection, access control, modularity
class myAccount:

    __balance = 0

    def deposit(self, amount):
        if amount>0:
            self.__balance += amount
            print("Deposit Success")
        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        if amount>0 and amount<=self.__balance:
            self.__balance -= amount
            print("Withdraw Successful")
        else:
            print("insufficient Balance")

    def check_balance(self):
        return self.__balance


obj = myAccount()
obj.deposit(100)
print(obj.check_balance())
obj.withdraw(30)
print(obj.check_balance())


################################################

