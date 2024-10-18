# class firstcode:

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

class firstcode:

    a=10
    b=20
    
 
    def display(self,x):
        print("Hello World!!", self.a + self.b + x )

    def show(self):
        result = self.display(5)
        print(result)

obj = firstcode()
obj.display(25)
obj.show()