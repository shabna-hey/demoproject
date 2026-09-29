###append ('a')#######
# f=open('k.txt','a')
# f.write('  python')
# f.close()


# #write a program to read the content from one txt file and add that content into another file
# f2 = open("second.txt", "r")
# s = f2.read()
# f2.close()

# f1 = open("first.txt", "a")
# f1.write(s)
# f1.close()
##tell() and seek()############
# f=open('k.txt','a+')
# print(f.tell())
# f.write("python")
# print("after write",f.tell())
# f.seek(0)
# print("after file pointer change",f.tell())
# print(f.read())
# f.close()



#remove##file#########################

# import os
# os.remove("k.txt")
# print("file is deleted")

# def add():
#     n1 = int(input("Enter the no: "))
#     n2 = int(input("Enter the no: "))
#     s = n1 + n2
#     print("Sum", s)
#
#
# def sub():
#     n1 = int(input("Enter the no: "))
#     n2 = int(input("Enter the no: "))
#     s = n1 - n2
#     print("Difference", s)

#
# def mul():
#     n1 = int(input("Enter the no: "))
#     n2 = int(input("Enter the no: "))
#     s = n1 * n2
#     print("Multiplication", s)
#
#
# def div():
#     n1 = int(input("Enter the no: "))
#     n2 = int(input("Enter the no: "))
#     s = n1 / n2
#     print("Division", s)
# while True:
#     print("1. Add")
#     print("2. Sub")
#     print("3. Mul")
#     print("4. Div")
#     print("5. Exit")
#
#     ch = int(input("Enter the choice: "))
#
#     if ch == 1:
#         add()
#
#     elif ch == 2:
#         sub()
#
#     elif ch == 3:
#         mul()
#
#     elif ch == 4:
#         div()
#
#     elif ch == 5:
#         exit()
#
#     else:
#         print("Invalid choice")


#menu driven ### function using
def read():
    f = open("sample.txt", "r")
    print("enter the file name")
    data = f.read()
    print(data)
    f.close()


def write():
    f = open("sample.txt", "w")
    data = input("Enter the content: ")
    f.write(data)
    f.close()
    print("Data written successfully")


def append():
    f = open("sample.txt", "a")
    data = input("Enter the content: ")
    f.write("\n" + data)
    f.close()
    print("Data appended successfully")


def search():
    f = open("sample.txt", "r")
    data = f.read()
    word = input("Enter the word to search: ")

    if word in data:
        print("Word found")
    else:
        print("Word not found")

    f.close()


def delete():
    import os
    os.remove("sample.txt")
    print("File deleted successfully")


while True:
    print("\n1. Read")
    print("2. Write")
    print("3. Append")
    print("4. Search")
    print("5. Delete")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        read()

    elif ch == 2:
        write()

    elif ch == 3:
        append()

    elif ch == 4:
        search()

    elif ch == 5:
        delete()

    elif ch == 6:
        exit()

    else:
        print("Invalid choice")