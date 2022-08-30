
user_input='random'

data={'english':['aasfa','GHTPW'],'urdu':['Alama Iqbal','7865']}

def showmenu():
    print("\n\t--------Book Record Library---------")
    print("\t~~Menu~~ ")
    print("1. Show all Records: ")
    print("2. Show name of the books: ")
    print("3. Show author of the book: ")
    print("4. Show ISBN number: ")
    print("5. Add New Book To Record: ")
    print("6. Update record: ")
    print("7. Delete Record: ")
    print("8. Exit: ")


while user_input != '8':

    showmenu()
    user_input=input("\tEnter your Choice: ")

    if user_input == '1':
        print("All Record: ")
        print(data)
    elif user_input == '2':
        item = print("Name of the Book: ")
        print(list(data.keys()))
    elif user_input == '3':
        item = input("Enter Name of the book: ")
        if item in data:
            print("Author: ",data[item][0])
        else:
            print("invalid choice")
    elif user_input == '4':
        item = input("Enter Name of the Book: ")
        if item in data:
            print("ISBN number: ",data[item][1])

    elif user_input == '5':
        print("Add New Book to Record")
        a = input("Book name: ")
        b = input("Author name: ")
        c = input("ISBN number: ")
        data[a] = b,c
        print("Book Added Successfully")
    elif user_input == '6':
        print("Update Record")
        a = input("Book name: ")
        b = input("Author name: ")
        c = input("ISBN number: ")
        data.update({a : [b,c]})
        print("Book updated successfully")
    elif user_input == '7':
        d = input("Enter name of the Book you want to Delete: ")
        del data[d]
        print("Book Deleted successfully")
    elif user_input == '8':
        print("\t~Good Bye~")