#static
# class Person:                         __init__:-initionalization properteis
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#
#     def show(self):          #current object
#         print(self.name,self.age)
#
#
# p1=Person("arun",24)   #create  object of class person
# p2=Person("anu",45)     #it will call __init__() automatically
# p1.show()
# p2.show()
from threading import active_count


#dynamic
# class Person:
#     def __init__(self):
#         self.name=input("enter the name")
#         self.age=input("enter the age")
#
#     def show(self):          #current object
#         print(self.name,self.age)
#
# p1=Person()
# p2=Person()
# p1.show()
# p2.show()


#define a class named employee with attributes empid,name,age,olace,salary,designationa
#and method getsalary() and showpersonaldetails
#create an empolyee object and call the methods
#
# class Employee:
#     def __init__(self):
#         self.empid=int(input("enter the id"))
#         self.name=input("enter the name")
#         self.age=input("enter the age")
#         self.place=input("enter the place")
#         self.salary=int(input("enter the salary"))
#         self.designation=input("enter the designation")
#     def getsalary(self):
#         print("salary",self.salary)
#     def showpersonaldetails(self):
#         print("name",self.name,"age",self.age,"place",self.place)
#
# e=Employee()
# e.getsalary()
# e.showpersonaldetails()



#define a class named student with attributes rollno,name,mark1,mark2,mark3 and methods
#display() to display roll no and total work of a student
#create 2 student objects and call the method

# class Student:
#     def __init__(self):
#         self.rollno=int(input("enter the number"))
#         self.name=input("enter the name")
#         self.mark1=int(input("enter the mark1"))
#         self.mark2 = int(input("enter the mark2"))
#         self.mark3 = int(input("enter the mark3"))
#     def display(self):
#         print("rollno",self.rollno,"total mark",self.mark1+self.mark2+self.mark3)
#
# s1=Student()
# s1.display()
# s2=Student()
# s2.display()

#define a class named book with attributes title,author,price,pages,languaguage
#and methods gettitle(),getauthor(),getprice()
#settitle,setauthor(),setprice()
#create book object and call the methods

#
# class Book:
#     def __init__(self):
#         self.title = input("Enter the title: ")
#         self.author = input("Enter the author: ")
#         self.price = int(input("Enter the price: "))
#         self.pages = int(input("Enter the pages: "))
#         self.language = input("Enter the language: ")
#
#     def gettitle(self):
#         print("Title:", self.title)
#
#     def getauthor(self):
#         print("Author:", self.author)
#
#     def getprice(self):
#         print("Price:", self.price)
#
#     def settitle(self):
#         self.title = input("Enter new title: ")
#         self.gettitle()
#     def setauthor(self):
#         self.author = input("Enter new author: ")
#         self.getauthor()
#     def setprice(self):
#         self.price = int(input("Enter new price: "))
#         self.getprice()
#
# b = Book()
# b.gettitle()
# b.settitle()


#1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user.
# Define the following methods:
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#Create an object of the Circle class and call both methods to display the results.
#
# class Circle:
#     def __init__(self):
#         self.radius = float(input("Enter the radius: "))
#
#     def getarea(self):
#         area = 3.14 * self.radius * self.radius
#         print("Area:", area)
#
#     def getperimeter(self):
#         perimeter = 2 * 3.14 * self.radius
#         print("Perimeter:", perimeter)
#
#
# c = Circle()
#
# c.getarea()
# c.getperimeter()

# 2.Create a class named Account with attributes acctnumber, acctname, and balance.
# Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.
# class Account:
#     def __init__(self):
#         self.acctnumber = input("Enter account number: ")
#         self.acctname = input("Enter account name: ")
#         self.balance = float(input("Enter balance: "))
#
#     def withdraw(self):
#         amount = float(input("Enter withdrawal amount: "))
#
#
#         if amount > self.balance:
#             self.balance = self.balance - amount
#             print("Withdrawal successful")
#         else:
#             print("Insufficient balance")
#
#     def deposit(self):
#         amount = float(input("Enter deposit amount: "))
#         self.balance = self.balance + amount
#         print("Deposit successful")
#
#     def showbalance(self):
#         print("Current balance:", self.balance)
#
#
# a1 = Account()
# #
# a1.withdraw()
#
#
# #
# a1.deposit()
# a1.showbalance()
# a2=Account()
# #ooro object details
# #a1.account()
#
#
# l=[a1,a2]
#for i in l:
    #print(i.accotnumber,i.acctname,i.balance)
    # i.showbalance()

# for i in l:
#     #for a specific object
#     if i.acctnumber==123:
#         i.showbalance()

#write a menu driven code for bank operation
#using class and list
# 1.create a new account
#2.withdraw
#3.deposit
#4.showbalance
#5.exit


#
# class Account:
#     def __init__(self):
#         self.acctnumber = input("Enter account number: ")
#         self.acctname = input("Enter account name: ")
#         self.balance = float(input("Enter balance: "))
#
#     def withdraw(self):
#         amount = float(input("Enter withdrawal amount: "))
#
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#             print("Withdrawal successful")
#         else:
#             print("Insufficient balance")
#
#     def deposit(self):
#         amount = float(input("Enter deposit amount: "))
#         self.balance = self.balance + amount
#         print("Deposit successful")
#
#     def showbalance(self):
#         print("Current balance:", self.balance)
#
#
# accounts = []
#
# while True:
#     print("\n--- BANK MENU ---")
#     print("1. Create new account")
#     print("2. Withdraw")
#     print("3. Deposit")
#     print("4. Show balance")
#     print("5. Exit")
#
#     ch = int(input("Enter the choice: "))
#
#     if ch == 1:
#         a = Account()
#         accounts.append(a)
#         print("Account created successfully")
#
#     elif ch == 2:
#         accno = input("Enter account number: ")
#
#         for a in accounts:
#             if a.acctnumber == accno:
#                 a.withdraw()
#                 break
#         else:
#             print("Account not found")
#
#     elif ch == 3:
#         accno = input("Enter account number: ")
#
#         for a in accounts:
#             if a.acctnumber == accno:
#                 a.deposit()
#                 break
#         else:
#             print("Account not found")
#
#     elif ch == 4:
#         accno = input("Enter account number: ")
#
#         for a in accounts:
#             if a.acctnumber == accno:
#                 a.showbalance()
#                 break
#         else:
#             print("Account not found")
#
#     elif ch == 5:
#         print("Thank you")
#         break
#
#     else:
#         print("Invalid choice")



###################################################################################################################

#define a class named employee with attributes empid,name,age,place,salary,designationa
#and method getsalary() and showpersonaldetails
#create an empolyee object and call the methods
# class Employee:
#     def __init__(self,e,n,a,p,s,d):
#
#         self.empid=e
#         self.name=n
#         self.age=a
#         self.place=p
#         self.salary=s
#         self.designation=d
#     def Show(self):
#         print(self.empid,self.name,self.age,self.place,self.designation)
#
#     def Getsalary(self):
#         print(self.salary)
# e=Employee(56,'arun',23,'malap',200000,'developer')
# e.Getsalary()
# e.Show()



#define a class named student with attributes rollno,name,mark1,mark2,mark3 and methods
#display() to display roll no and total work of a student
#create 2 student objects and call the method
#
# class Student:
#     def __init__(self,r,n,m1,m2,m3):
#         self.rollno=r
#         self.name=n
#         self.mark1=m1
#         self.mark2=m2
#         self.mark3=m3
#     def Display(self):
#         print("roll no:",self.rollno,"\n","name:",self.name,"\n","mark 1:",self.mark1,"\n","mark 2:",self.mark2,"\n","mark 3:",self.mark3)
#
#     def Total_mark(self):
#         print("total mark:",self.mark1+self.mark2+self.mark3)
#
# s=Student('12','shabna',21,23,11)
# s.Display()
# s.Total_mark()

#define a class named book with attributes title,author,price,pages,languaguage
#and methods gettitle(),getauthor(),getprice()
#settitle,setauthor(),setprice()
#create book object and call the methods
# class Book:
#     def __init__(self,t,a,p,pa,l):
#         self.title=t
#         self.author=a
#         self.price=p
#         self.pages=pa
#         self.language=l
#     def GetTitile(self):
#         print(self.title)
#     def GetAuthor(self):
#         print(self.author)
#
#     def GetPrice(self):
#         print(self.price)
#
#     def SetTitile(self,t):
#         self.titile=t
#         self.GetTitile()
#     def SetAuthor(self,a):
#         self.author=a
#         self.GetAuthor()
#     def SetPrice(self,p):
#         self.price=p
#         self.GetPrice()
#
#
# b=Book('abc','rathor',34,22,'malayalm')
# b.GetTitile()
# b.GetAuthor()
# b.GetPrice()
#
# b.SetTitile("python")
# b.SetAuthor("alli")
# b.SetPrice("300")
#
#


#1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user.
# # Define the following methods:
# # getarea() – to calculate and display the area of the circle.
# # getperimeter() – to calculate and display the perimeter (circumference) of the circle.
# #Create an object of the Circle class and call both methods to display the results.
# class Circle:
#     def __init__(self,r):
#         self.radius=r
#
#
#     def getarea(self):
#         area=3.14*self.radius*self.radius
#         print("area",area)
#     def getperimeter(self):
#         perimeter=2*3.14*self.radius
#         print("perimeter",perimeter)
#
# c=Circle(5)
# c.getarea()
# c.getperimeter()

# .Create a class named Account with attributes acctnumber, acctname, and balance.
# Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal
# and deposit operations and display the updated balance.
# class Bank:
#     def __init__(self,a,an,b):
#         self.accno=a
#         self.accname=an
#         self.balance=b
#
#     def Withdraw(self):
#          amount=1000
#          if amount<=self.balance:
#              self.balance=self.balance-amount
#              print("withdraw",amount)
#          else:
#              print("incifient")
#
#     def deposit(self):
#         amount=100
#         self.balance=self.balance+amount
#         print("deposit",amount)
#
#     def showbalance(self):
#         print(self.balance)
# b=Bank(25589,'shabna',600000)
# b.Withdraw()
# b.deposit()
# b.showbalance()




















