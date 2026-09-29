###inheritance#######:-one class into another class
#class A:
        #statements



#class B(A):
       #statements

####################################################################################################
#syntax##
# class Parent:
#     def m1(self):
#         print("in Perant class method m1")
#     def m2(self):
#         print("in perant class method m2")
#
#
# class Child(Parent):
#     def m1(self):
#         super().m1()                         #overriding
#         print("in child class m1")            #modify or extention
#      def m3(self):
#         print("in child class m3")
#
# c=Child()
# c.m1()
# c.m2()
# c.m3()

#parent(name,age),child(rollno,couse,mark)
# class Person:
#     def __init__(self):
#         self.name=input("enter the name")
#         self.age=int(input("enter the age"))
#     def show(self):
#         print(self.name,self.age)
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("enter the rollno"))
#         self.couse=input("enter the couse")
#         self.mark=int(input("enter the mark"))
#     def show(self):
#         super().show()
#         print(self.rollno,self.couse,self.mark)
#
#     def updatemark(self):
#         self.mark=int(input("enter the mark"))
#
#
# s=Student()
# s.show()
# s.updatemark()
# s.show()


# single inheritance#######################################################################################################
# class Company:
#     def __init__(self):
#         self.compname=input("enter the comapany name")
#         self.location=input("enter the location ")
#     def show(self):
#         print(self.compname,self.location)
#
#
# class Employee:
#     def __init__(self):
#         super().__init__()
#         self.empid=int(input("enter the id"))
#         self.name=input("enter the name")
#         self.designation=input("enter the designation")
#         self.salary=int(input("enter the salary"))
#     def display(self):
#         print(self.empid,self.name,self.designation,self.salary)
#
#     def updatesalary(self):
#         self.salary = self.salary * 1.10
#         self.salary = int(self.salary)
#         print("Updated salary:", self.salary)
#
#
# class Category:
#     def __init__(self):
#
#         self.categoryname=input("enter the category name")
#
#     def show_category(self):
#         print("category name",self.categoryname)
#
#
# class Product:
#     def __init__(self):
#         super().__init__()
#         self.Product=input("enter the productname")
#         self.price=int(input("enter the price"))
#         self.quantity=int(input("entre the quantity no"))
#     def total_price(self):
#
#         print(self.Productname,self.price*self.quantity)
#
# p=Product()
# p.total_price()
# p.show_category()

##multiple inheritance##################################################################################################

# class Hospital:
#     def __init__(self):
#         self.hos_name=input("enter the hos name")
#         self.location=input("enter the location")
#         self.phoneno=int(input("enter the phno"))
#     def display_Hospital(self):
#         print(self.hos_name,self.location,self.phoneno)
# class Department:
#     def __init__(self):
#         self.dept_name=input("entre the deptname")
#         self.doctor_name=input("enter the doctname")
#     def Display_Department(self):
#         print(self.dept_name,self.doctor_name)
#
#
# class Patient(Hospital,Department):
#     def __init__(self):
#         Hospital.__init__(self)
#         Department.__init__(self)
#
#
#         self.patient_name=input("enter the patient name")
#         self.age=int(input("enter the age"))
#         self.gender=input("enter the gender")
#         self.admission_date=input("enter the admission no")
#         self.bedno=int(input("enter the bed no"))
#         self.discharge_date=""
#
#
#     def full_summary(self):
#         Hospital.display_Hospital(self)
#         Department.Display_Department(self)
#
#         print(self.patient_name, self.age, self.gender, self.admission_date, self.bedno, self.discharge_date)
#         if self.discharge_date=="":
#             print("not yet discharge")
#         else:
#             print("discharge date",self.discharge_date)
#     def set_discharge(self):
#         self.discharge_date=input("enter the discharge date")
#
# p=Patient()
# p.full_summary()
# p.set_discharge()
# p.full_summary()

#####abstraction##########################################################################################################################

# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def get_perimeter(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self):
#         self.length=int(input("enter the length"))
#         self.breadth=int(input("enter the breadth"))
#     def get_area(self):
#         print("area",self.length*self.breadth)
#
#     def get_perimeter(self):
#         print("perimeter",2*(self.length+self.breadth))
# class Square(Shape):
#     def __init__(self):
#         self.side=int(input("enter the side"))
#     def get_area(self):
#         print("area of square",self.side*self.side)
#     def get_perimeter(self):
#         print("perimeter",4*self.side)
#
#
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
#
#
# s=Square()
# s.get_area()
# s.get_perimeter()
#
# from abc import ABC,abstractmethod
#
# class Employee(ABC):
#     @abstractmethod
#     def __init__(self):
#             self.name = input("enter the name")
#             self.age = int(input("enter the age"))
#             self.empid = int(input("enter the empid"))
#     @abstractmethod
#     def Calculate_salary(self):
#         pass
#
# class FullTimeEmployee(Employee):
#     def __init__(self):
#         super().__init__()
#         self.monthly_salary=int(input("enter the salary"))
#     def Calculate_salary(self):
#         print("salary",self.monthly_salary)
# class PartTimeEmployee(Employee):
#
#     def __init__(self):
#         super().__init__()
#         self.rate=int(input("enter the rate"))
#         self.houre=int(input("enter the houre"))
#     def Calculate_salary(self):
#         print(self.houre*self.rate)
#
#
# f=FullTimeEmployee()
# f.Calculate_salary()
#
#
# p=PartTimeEmployee()
# p.Calculate_salary()




