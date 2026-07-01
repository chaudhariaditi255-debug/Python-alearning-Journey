
contact = {}

contact["name"] = input("Enter Name: ")
contact["phone"] = input("Enter Phone Number: ")
contact["email"] = input("Enter Email: ")
contact["city"] = input("Enter City: ")

while True:
    print("1. Show Contact")
    print("2. Update Phone Number")
    print("3. Exit")

    choice = input("Enter your choice: ")
    

    if choice == "1":
        print("Name :", contact["name"])
        print("Phone :", contact["phone"])
        print("Email :", contact["email"])
        print("City :", contact["city"])

    elif choice == "2":
        new_phone = input("Enter New Phone Number: ")
        contact["phone"] = new_phone

    elif choice == "3":
        break

    else:
        print("Invalid Choice! Please try again.")
