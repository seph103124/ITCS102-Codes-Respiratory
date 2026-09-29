#input

age = int(input("age --> "))
monthly_revenue = float(input("monthly revenue ---> "))
credit_score = int(input("credit score --->"))
years_in_business = float(input("year of business ---> "))
has_defaults = bool(input("has a defaults ---->  "))
collateral = input("collateral name ---> ")
collateral_value = float(input("collateral value --> "))

#baseline age >= 21 , years >= 2.0 , False in defaults
max_loan = 0
base_fee = 0

if age >= 21 and years_in_business >= 2.0 and has_defaults == False:
    print("baseline passed")
    if credit_score >= 720:
        max_loan = monthly_revenue * 3
        print("maximum loanable amount is set to",max_loan)
        print("high credit score")
        if monthly_revenue >= 50000:
            print("monthly revenue higher than 50k")
            base_fee = max_loan * 0.015
            print("base fee rate is set to", base_fee)
        else:
            print("revenue lower than 50k")
            base_fee = max_loan * 0.025
            print("base fee rate is to", base_fee)

            #collateral
            if collateral_value >= max_loan:
                print("collateral ",collateral, " with a value of ", collateral_value, "is accepted")
            else:
                print("Rejected: insufficiend collateral value for ", collateral)


            #surcharge
            surge_fee_rate = max_loan * base_fee
            print("Additional charge of ",surge_fee_rate)
            if max_loan % 5000 != 0:
                print("Additional charge added")
                surge_fee_rate += 250
                print("updated base fee is ", surge_fee_rate)    
    elif credit_score >= 620 and credit_score < 720: #tier 2
        print("maximum loan for this credit score is", max_loan)
        if years_in_business >= 5.0:
            print("business is more than 5 years")
            base_fee = max_loan * 0.02
            print("base fee rate is set to", base_fee)
        else:
            print("business is lower than 5 years")
            base_fee = max_loan * 0.035
            print("base fee is set to", base_fee)
            #collateral
            if collateral_value >= max_loan:
                print("collateral ",collateral, " with a value of ", collateral_value, "is accepted")
            else:
                print("Rejected: insufficiend collateral value for ", collateral)
            
            
                        #surcharge
            urge_fee_rate = max_loan * base_fee
            print("Additional charge of ",surge_fee_rate)
            if max_loan % 5000 != 0:
                print("Additional charge added")
                surge_fee_rate += 250
                print("updated base fee is ", surge_fee_rate) 
    elif credit_score < 620: #Tier 3
        print("your credit score is to low")
    else:
        print("invalid")
else:
    print("baseline failed")

