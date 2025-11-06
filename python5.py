monthly payment = 0
loan amount = 0
interest rate = 0 
number of payments = 0 

#Demo for calculating monthly payment for a loan
loan amount = float(input("Please enter the loan amount: "))
interest rate = float(input("Please enter the interest rate (as a percentage): "))
number of payments = int(input("please enter the number of payments (months): "))

#calculation for number of payments
interest rate = interest rate / 100 / 12 #Convert annual percentage rate to a monthly decimal rate 

monthly payment = (loan amount * [interest rate*(1 + interest rate)*number of payment])/([1+ interest rate]* number of payment-1 )

#printting the monthly payment 
print("Your monthly payment would be {0:f2}".format(monthly payment))
