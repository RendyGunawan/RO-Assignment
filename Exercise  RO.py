rows = eval(input("How many lines do you want:"))
for x in range(rows):
    print(" "*(rows-x),end="")
    for y in range(1,x+2):
        print("*",end="")
    print()