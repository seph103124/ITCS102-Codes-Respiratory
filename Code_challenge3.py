name = input("sender name ---> ")
item = input("what kind of items ---> ")
is_fragile = bool(input("it is fragile (if is not press enter) --->"))
weight = float(input("what is weight? (kg) --->"))
distance = float(input("how far in warehouse (km) --->"))
is_express = bool(input("it is express (press enter if not) --->"))
is_international = bool(input("international (press enter if not) --->"))

#calculate cost base

base_cost = (weight * 2.5) + (distance * 0.15)

#evaluate pricing tiers (apply the first matching only)

#free shipping

if weight <= 2 and distance <= 100 and is_express == False and is_international == False:
    print("Free shipping")
    total = 0

#international express

elif is_international == True and is_express == True:
    print("Parcel express to international applied")
    Total = (base_cost * 1.4) + 50
    
#express or heavy international

elif is_express == True or is_international == True and weight > 20:
    print("Parcel is express or heavy international applied")    
    Total = (base_cost * 1.20) + 25
    
#Oversized

elif weight > 30 or distance > 1000:
    print("Oversize applied")
    Total = base_cost + 30
    
#Standard rate

else:
    print("standard rate is applied")    
    Total = base_cost
      
      
    print("Name of sender : ", name)
    print("Name of item : ", item)
    print("Over all total : peso ", Total)
