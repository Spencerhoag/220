def monthly_interest():
    annual_interest_rate = eval(input("Enter the annual interest rate of your credit card as a percentage: "))
    days_in_billing_cycle = eval(input("Enter the total amount of days in your billing cycle: "))
    net_balance = eval(input("Enter your previous/net balance: "))
    payment_amount = eval(input("Enter the total amount deposited into your account: "))
    billing_cycle_date = eval(input("Enter the day of the billing cycle in which payment was made: "))
    days_before_end_cycle = days_in_billing_cycle - billing_cycle_date
    step3 = (net_balance * days_in_billing_cycle) - (payment_amount * days_before_end_cycle)
    average_daily_balance = step3 / days_in_billing_cycle
    mir = annual_interest_rate / 12
    mir_decimal = mir / 100
    monthly_interest_charge = average_daily_balance * mir_decimal
    print("Your monthly interest charge is $", monthly_interest_charge)
