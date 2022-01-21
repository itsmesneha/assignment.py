#function 1
def display_datatypes (i,f,b,list,tup,set,dictionary):
    print(f"The integer value is : {i}")
    print(f"The float value is : {f}")
    print(f"The boolean value is : {b}")
    print(f"The list is : {list}")
    print(f"The tuple is : {tup}")
    print(f"The set is : {set}")
    print(f"The dictionary is : {dictionary}")

display_datatypes(5,7.8,True,[1,2,3,4],(10,20,40),{100,101,102,103,104},{4:"four",5:"five",6:"six"})

print(" ")

#function 2
def create_dict(dictionary1):
    print(f"The details of the information are: ")
    for key in dictionary1:
        print(f"Key:{key} , Value:{dictionary1[key]}")

create_dict({'Name':'Sneha','age':'20','gender':'female','education':'Engineering'})

print(" ")

#function 3
def take_inputs(x,y):
    list1=[x,y]
    print(f"The given list is : {list1}")

take_inputs(5,6)
