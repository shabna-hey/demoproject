#sum of two numbers
# try:
#     n1=int(input("enter the number"))
#     n2=int(input("enter the number"))
#     s=n1+n2
#
# except:
#     print("invalid number")
# else:
#     print("sum",s)
# finally:
#     print("done")

#division two numbers
# try:
#      n1=int(input("enter the number"))
#      n2=int(input("enter the number"))
#      s=n1/n2
#      print(R)
# except ZeroDivisionError:
#     print("zero division error")
# except ValueError:
#     print("value error")
#
# except:
#     print("Error")


# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
# while(True):
#
#
#     try:
#
#             import math
#             n=int(input("enter the number"))
#             a=math.factorial(n)
#             print("factorial",a)
#             break
#     except ValueError:
#         print("value error")
#
#     except:
#         print("error")





# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.
# try:
#     n1 = int(input("Enter the no: "))
#     n2 = int(input("Enter the no: "))
#
#     print("1.addition")
#     print("2.substract")
#     print("3.multiplication")
#     print("4.division")
#     print("5.exit")
#
#     ch=int(input("enter the choice"))
#      if ch in [1,2,3,4]:
#     if ch==1:
#         print(n1+n2)
#     elif ch==2:
#         print(n1-n2)
#     elif ch==3:
#         print(n1*n2)
#     elif ch==4:
#         print(n1/n2)
#     elif ch==4:
#         print("exit")
#     else:
#         print("invalid")
#
# except ValueError:
#     print("value error")
# except ZeroDivisionError:
#     print("zero division error")






# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist
# try:
#     f = open("data.txt", "r")
#     content = f.read()
#     print(content)
#     f.close()
#
# except FileNotFoundError:
#     print("File does not exist")



#Given a Dictionary
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist
# try:
#     d={"name":"arun","age":23,"place":"ekm"}
#     n=input("enter the key")
#     print(d[n])
# except KeyError:
#     print("key error ")
# except:
#     print("invalid")




# try:
#     n1=int(input("enter the number"))
#     n2=int(input("eneter the number"))
#     s=n1/n2
# except ZeroDivisionError as s:
#     print(s)
#     print(type(s))
# except ValueError as e:
#     print(e)
#     print(type(e))
# except Exception as e:
#     print(e)
#     print(type(e))


# Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"
# try:
#     n=int(input("enter the number"))
#     if n<=0:
#         raise ValueError("number must be positive")
#     else:
#         print(n)
# except ValueError as e:
#     print(e)
#     print(type(e))
#
#
#
#
# #Ask the user to enter a password.if its length is less than 8 characters ,raise
# #a customexception InvalidPasswordError with the message ("Password should be 8
# # characters")
# class InvalidPassword(Exception):
#     pass
# try:
#     n=int(input("enter the password"))
#     if n<=8:
#         raise InvalidPassword("password should be 8 characters")
#     else:
#         print(n)
# except InvalidPassword as e:
#     print(e)
#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")


# class InsuffientBalanceError(Exception):
#     pass
# balance=50000
# a=int(input("enter the amount"))
# try:
#     if a<balance:
#         raise InsuffientBalanceError("not enough balance.transaction failed")
#     else:
#         print(a)
# except InsuffientBalanceError as e:
#     print(e)

