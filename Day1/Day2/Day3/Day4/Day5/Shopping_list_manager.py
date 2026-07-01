print("Shopping List Manager")

Item_list = ["Milk","Sugar","Bread"]

while True:
    
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show List")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        Item_list.append(item)
        

    elif choice == "2":
        item = input("Enter item to remove: ")

        if item in Item_list:
            Item_list.remove(item)  
        else:
            print("Item not found!")

    elif choice == "3":
        print(" Item List:")

        if len(Item_list) == 0:
            print("List is empty")
        else:
            for item in Item_list:
                print(item)

    elif choice == "4":
        break

    else:
        print("Invalid Choice!")

