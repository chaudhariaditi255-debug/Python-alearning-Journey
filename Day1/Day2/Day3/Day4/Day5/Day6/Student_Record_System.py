
print("----- Student Record System -----")

student = {}

student["name"] = input("Enter Name: ")
student["marks"] = int(input("Enter Marks: "))
student["branch"] = input("Enter Branch: ")

print("Name   :", student["name"])
print("Marks  :", student["marks"])
print("Branch :", student["branch"])

if student["marks"] >= 90:
    print("Outstanding")

elif 75 <= student["marks"] <= 89:
    print("Excellent")

elif 60 <= student["marks"] <= 74:
    print("Good")
else:
    print("needs Improvement")
