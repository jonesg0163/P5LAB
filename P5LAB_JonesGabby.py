# Gabby Jones
# 11/11/2025
# P5Lab
#Using integer division and if/else statements

import random


def calculate_change(change):

    #Convert the float value into an integer
    change = int(change * 100)

    # print(change)

        
    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed
    #integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed

    if num_dollars > 0:
        print(num_dollars,  end=" ")
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")
            
    if num_quarters > 0:
        print(num_quarters,  end=" ")
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")

    if num_dimes > 0:
        print(num_dimes,  end=" ")
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")

    if num_nickles > 0:
        print(num_nickles,  end=" ")
        if num_nickles == 1:
            print("Nickle")
        else:
            print("Nickles")

    if num_pennies > 0:
        print(num_pennies,  end=" ")
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")

# Define the main function
def main():
    # Generate a random value for cart total
    cart_total = round(random.uniform(0.01, 100.00), 2)
    print(f"Your total is: ${cart_total}")
    print()
    # Get cash in from user
    cash_in = float(input("Cash Entered: $"))
    
    # Calculate change owed
    customer_change = cash_in - cart_total
    
    # Display customer change
    print(f"Change owed to customer: ${customer_change:.2f}")
    
    # Call the function to calculate change
    calculate_change(customer_change)
    
# Call the main
main()

