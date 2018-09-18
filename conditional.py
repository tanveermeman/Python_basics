#This will have examples of the conditional statemants.

# if a < b :
#     print(f'{a} is less than {b}')


a=input("enter side of a triangle a = ")
b=input("enter side of a triangle b = ")
c=input("enter side of a triangle c = ")
if a != b and b != c and c != a:
    print("This is a scalene triangle")

if a == b and b== c and c == a:
    print("This is a equiateral triangle.")




