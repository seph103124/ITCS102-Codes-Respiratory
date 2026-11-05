size = int(input("Size of diamond ---> "))
for x in range(1, size + 1):
    for y in range(size - x):
        print(" ", end="")
    for z in range(2 * x - 1):
        print("*", end="")
    print() 
    if x == size:
            for a in range(size - 1, 0, -1):
                for b in range(size - a):
                    print(" ", end="")
                for c in range(2 * a - 1):
                    print("*", end="")
                print()
