from functions import menu, add, search, delete, list_all

while True:
    try:
        menu()
        opt = int(input("Insert an option: "))
        if opt == 1:
            add()
        elif opt == 2:
            search()
        elif opt == 3:
            delete()
        elif opt == 4:
            list_all()
        elif opt == 5:
            break
        else:
            print("Invalid option, try again.")
    except ValueError:
        print("Invalid option, try again.")