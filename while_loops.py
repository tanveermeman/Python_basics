from pip._vendor.distlib.compat import raw_input

i = 0
while i < 5:
    print(f"i is {i}",end="         ")
    i+=1


x = 0
while x * x < 30:
    print(x*x,end=" ")
    x+=1

def print_cubes_upto_limit(limit):
    i=0
    while i*i*i < limit:
        print(i*i*i)
        i+=1

limit = int(input("enter a limit "))
print_cubes_upto_limit(limit)