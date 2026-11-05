sum = 0

back = True
while back == True:
    yes = int(input("Enter a number ---> "))

    if back == 0:
        print("the loopp is terminated")
        print("the sum of the numbers is ---> ",sum)
        break
    else:
        print("continue the loop")
        sum += yes
        print("the sum of the numbers is ---> ",sum)
        continue