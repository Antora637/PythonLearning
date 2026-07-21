# class Student:
  
#    def __init__(self, name):
#       self.name = name
     
# s1 = Student("Antora")
# print (s1.name)
# # del s1.name
# # print(s1.name)

# class Account:
#     def __init__(self, acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass #__ diye private hoye jay

#     def reset_pass(self):
#         print(self.__acc_pass)


# acc1 = Account("12345","abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass())

# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()

# p1 = Person()

# print(p1.welcome())


##Inheritance

#single inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class ToyotaCar(Car):     #inherit korlam
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# print(car1.start())
              

#multi level inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class ToyotaCar(Car):     #inherit korlam
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type = type
        

# car1 = Fortuner("diesel")

# print(car1.start())


#multiple inheritance
# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A,B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


##super method
# class Car:

#      def __init__(self,type):
#         self.type = type

#      @staticmethod
#      def start():
#         print("car started..")

#      @staticmethod
#      def stop():
#         print("car stopped..")

# class ToyotaCar(Car):     #inherit korlam
#     def __init__(self, name,type):
#         super().__init__(type)
#         self.name = name
#         super().start()
        
# car1 = ToyotaCar("Prius","electric")
# print(car1.type)


#class method
# class Person:
#     name = "anonymous"

#     # def changeName(self, name):
#     #     self.__class__.name = "Antora"  #class attribute change holo
#     #      # or Person likhleo hoto

#     #class method 
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Antora")
# print(p1.name)
# print(Person.name)


##property
# class Student:
#     def __init__(self,phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     # def calcPercentage(self):
#     #     self.percentage = str((self.phy + self.chem + self.math)/3) +"%"

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3) +"%"
    
# stu1 = Student(98,97,99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.percentage)


#Polymorphism###

#operator overloading
# print(1+2) #3
# print("Umme " + "Habiba") #concatenate
# print([1,2,3,4] + [4,5,6]) #merge


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self,num2):         #dunder funvtion __add__
        newReal = self.real +num2.real
        newImg = self.img +num2.img
        return Complex(newReal,newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1+num2
num3.showNumber()
