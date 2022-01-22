name=input(f"Name: ")
age=int(input(f"Age: "))
percent=float(input(f"percent: "))
dissabilities=bool(input(f"No Dissabilities?: "))
list=[name,age,percent,dissabilities]
tup=(name,age,percent,dissabilities)
dict={'Name':'Sneha','Age':20,'Percent':94.2,'Dissabilities':'True'}

print(" ")

print(f"String : {name}")
print(f"Integer : {age}")
print(f"Float : {percent}")
print(f"Boolean : {dissabilities}")
print(f"List : {list}")
print(f"Tuple : {tup}")
print(f"Dictionary : {dict}")
