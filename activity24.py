route = ["Terminal", "Perez park", "Pacific mall"]
passenger = []
SEATS = 6
FARE =13
total = 0

while True:
    print()
    print("Sakay:", passenger)
    print(len(passenger), "of", SEATS, "seats")
    print("1 Sakay 2 priority seat 4 para po!")
    print("4 baba sa pinto 5 nana sa harap")
    print("6 seat check 7 balikan 8 exit")
    choice = input("choice")

    if choice == "1":
        if len(passenger) == SEATS:
            print("Puno na!")
        else:
            name = input("Name")
            passenger.append(name)
            total = total + FARE
            print(name, "boarded at the back")


    elif choice == "2":
        if len(passenger) == SEATS:
            print("Puno na!")
        else:
            name = input("Name")
            passenger.insert(0,name)
            total = total + FARE
            print(name, "took the priority seat")


    elif choice == "3":
        name = input("who is getting off?")
        if name in passenger:
            passenger.remove(name)
            print(name, "got off. Ingat!")
        else:
            print(name, "is not on this jeep")

    elif choice == "4":
            if len(passenger) == 0:
                print("The jeep is empy")
            else:
                left = passenger.pop()
                print(left, "got off at the door")

    elif choice == "5":
                if len(passenger) == 0:
                    print("The jeep is empy")
                else:
                    front = passenger.pop(0)
                    print(front, "got off at the door")

    elif choice == "6":
        for i in range(len(passenger)):
            print("Seat", i + 1, passenger [i])

    elif choice == "7":
        route.reverse()
        print("route", route)

    elif choice == "8":
        print("Total fare today", total) 
        break
    else:
        print("Invalid choice")  











