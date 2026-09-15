age = int(input("Enter your Age --->  "))
is_employed = bool(input("Are you currently employed? (True/False) --->  "))
credit_score = int(input("What is your credit score? --->  "))
annual_income = float(input("What is your annual income? --->  "))
has_collateral = bool(input("Do you have collateral? (True/False) --->  "))

if age >= 21 and is_employed == True:
    print ("You are success to criteria")
    if credit_score >= 750: 
        print("You have a high credit score!")
        if annual_income >= 100000:
            base_rate = 4.5
            print("You have a high salary and high credit score, your interest is",base_rate)
        else: 
            base_rate = 5.0
            print("You have a high salary and high credit score, your interest is",base_rate)
    elif credit_score >= 600 and credit_score < 750:
        if has_collateral == True:
            base_rate = 7.0
            print("You have a high salary and high credit score, your interest is",base_rate)
        elif annual_income <= 40000:
            print("Low salary with fair credit score")
            base_rate = 9.5
            print("You have a low salary and fair credit score, your interest is ",base_rate)
        else:
            print("You have a fair credit score with no collateral")
            base_rate = 8.0
            print("You have a low salary and fair credit score, your interest is",base_rate)
    elif credit_score < 600:
        print("Rejected: Credit score too low!")
    else: 
        print("Failed")			
else:
    print("Rejected: Fails baseline criteria") 
