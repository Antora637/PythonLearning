# class Student:
#    college_name = "ABC college" #class attribute
#    def __init__(self, name, marks):
#       self.name = name
#       self.marks = marks #obj attribute
      
#    def welcome(self):
#       print("welcome students,", self.name)

#    def get_marks(self):
#       return self.marks
    

# s1 = Student("Antora",90)
# print(s1.name,s1.marks)
# print(Student.college_name) #or s1.college_name
# s1.welcome()
# print(s1.get_marks())

# s2 = Student()
# print(s2.name)

# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)


#student class. name ,marks of 3 subjects with constructor

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum = sum+val
#         print("Hi", self.name, "Your Average marks :",sum/3)
        
# s1 = Student("Antora", [91,71,98])
# s1.get_avg()

# s1.name = "Anto" #name change hoye jabe
# s1.get_avg()

#static method
# class staticMethod:
#     @staticmethod #decorator
#     def hello():
#         print("Hello world! ")
# h1 = staticMethod()
# h1.hello()


# #Abstruction
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started..")
        
# car1 =Car()
# car1.start()


#Bank account example
class Account:
    def __init__(self,bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Taka:", amount,"was debited")
        print("Total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Taka:", amount,"was credited")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(5000)


        