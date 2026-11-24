from activity25 import taga_triangle
from activity25 import box 
from activity25 import sum
from activity25 import my_factioral
import os
while True:
    print("MINI MENU")
    print("SELECT AN OPTION")
    print("1 - Triangle")
    print("2 - Sum")
    print("3 - box")
    print("4 - factorial")
    choose = int(input("Which option to go --->  "))


    if choose == 1:
        os.system("cls")
        print("taga_triangle")
        size = int(input("size ng triangle"))
        taga_triangle(size)
        continue
    elif choose == 2:
        os.system("cls")
        print("SIMPLE SUMMATION")
        num1 = int(input("number 1 -- > "))
        num2 = int(input("number 2 ---> "))
        print(f"the sum of {num1} and {num2} is {sum(num1, num2)}")
        continue
    elif choose == 3:
        os.system("cls")
        print("BOX")
        size = int(input("SIZE NG BOX"))
        box(size)
        continue
    elif choose == 4:
        os.system("cls")
        print("FACTORIAL")
        num = int(input("INTPUT ANY NUMBER --> "))
        print(f"The factorial of {num} is {my_factioral(num)}")
        continue
    elif choose == 5:
        print("SYSTEM EXIT")
        break
    else:
        print("INVALID CHOICE")
        continue