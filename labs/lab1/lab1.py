"""
Kelsey Thorvalson
lab1.py
This program is used to calculate a user's average daily balance and monthly interest charge on their credit card.
I certify that this assignment is entirely my own work.
"""

def monthly_interest():
    interest_rate = eval(input("Please enter the annual interest rate:"))
    interest = (interest_rate/12)/100
    billing_cycle = eval(input("Please enter the number of days in the billing cycle:"))
    net_balance = eval(input("Please enter the previous net balance of the account:"))
    net_billing = net_balance * billing_cycle
    net_payment = eval(input("How much was the payment received?"))
    day_received = eval(input("On what day of the billing cycle was the payment received?"))
    step2 = net_payment * (billing_cycle - day_received)
    step3 = net_billing - step2
    step4 = step3/billing_cycle
    balance = round(step4, 2)
    print("The average daily balance is $", balance)
    interest_charge = step4 * interest
    charge = round(interest_charge, 2)
    print("The monthly interest charge is $", charge)
