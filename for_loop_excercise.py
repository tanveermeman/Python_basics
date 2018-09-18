def print_a_number_triangle(number):
    for i in range(1,number + 1 ):
        for j in range(1, i + 1):
            print(j,end=" ")

        print()

number = int(input("Enter a number "))
print_a_number_triangle(number)
