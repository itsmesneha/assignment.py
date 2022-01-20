list=[]
print("Enter your details for the following: ")
name=input(f"Name: ")
age=int(input(f"Age: "))
gender=input(f"Gender: ")
address=input(f"Address: ")
education=input(f"Educational qualification: ")
list=[name,age,gender,address,education]
print("\n")
print(f"The information given by user is: ")
for i in list:
    print(i)
