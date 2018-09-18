x = int(input("enter first number"))
y = int(input("enter second number"))

print("""1 addition
2 subtraction
3 multiplication
4 division
5 exit""")

operation = int(input("enter a choice"))

while operation  != 5:

    if operation == 1:
        result = x+y

    elif operation == 2:
        result = x-y

    elif operation == 3:
        result = x*y

    elif operation == 4:
        result = x/y

    else :
        print("invalid choice")




    print(result , "is the result")

    operation = int(input("enter a choice"))

print("thank you")


