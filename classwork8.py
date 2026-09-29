 # #write a program to read a text file and displays the number of lines in a file

# f=open('k.txt','r')

# s=f.readlines()
# print(len(s))
# f.close()

# # #write a program to display the number of words in a file
# s=f.read()
# a=s.split()
# b=len(a)
# print(b)
# f.close()


 # write a program to update the second line in a file

# s=f.readlines()
# s[1]="second line updated\n"
# f.close()
# f=open('k.txt','w')
# f.writelines(s)
# f.close()



 # write a program to display the last 5 lines in file
# s=f.readlines()
# print(s[-5:])
# f.close()


# #program to search a particular word in a file
# s=f.readlines()
# if 'hello' in s:
#     print("Word found")
# else:
#     print("Word not found")
#
# f.close()


#find the number of letters,digits,and spaces in a file
#
# s=f.read()
# l=0
# d=0
# spa=0
# for i in s:
#     if i.isalpha():
#         l += 1
#     elif i.isdigit():
#         d += 1
#     elif i == " ":
#         spa += 1
#
# print(l)
# print(d)
# print(spa)
# f.close()

#reverse the lines in a file
#
# s=f.readlines()
# s.reverse()
# for i in s:
#     print(i,end=" ")
# f.close()

# A file totalstudents.txt contains the names of all students in a class,


# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # # Write their names to a new file named failed_students.txt, one name per line.
# f1=open("totalstudents.txt",'r')
# a=f1.readlines()
# f1.close()
# f2=open('passedstudents.txt','r')
# b=f2.readlines()
# f2.close()
# f3=open('failed_students.txt','w')
# for i in a:
#     if i not in b:
#         f3.write(i)
# f3.close()





