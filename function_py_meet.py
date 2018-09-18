def func():
    print("hello world!")

func()

#
# def addition(x,y):
#     return x+y
#
# print(addition(2,3))
#
# def scope(x,y):
#     x=x+y
#
# scope(2,3)
# print(x)# out of scope :cannot be accesed outside the scope() function.

# *******     Exceptions    *********
try:
    print(1/0)
except ZeroDivisionError:
    print("Not allowed")

# generic exception

try:
    print(1/0)

except Exception as e : # Exception catches any kind of exception that may occur.
    print(e)
    