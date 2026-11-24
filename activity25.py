

def taga_triangle(number):
    for x in range(number, 0, -1):
        for y in range(1, x + 1):
            print("*", end =" ")
        print( )



def sum(x, y):
    return x+y

def box(size):
    for x in range(size+1):
        for y in range(size + 1):
            if y == 0 or x == 0 or x ==size-1 or y == size -1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
box(2)
box(4)


def my_factioral(number):
    dect = 1
    for x in range(number, 0, -1):
        fact *= x
    return fact

print (my_factioral(3))

taga_triangle(12)
taga_triang(6)
taga_triangel(15)

print(sum(23, 2))
print(sum(16, 3) * 12)
