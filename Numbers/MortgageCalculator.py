# Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
#Also figure out how long it will take the user to pay back the loan.

import sys
#fixed term in months
def getMortgagePayment(principle, apr, terms):
	monthlyIntr = apr/12
	#use loan formula thing
	return (principle*monthlyIntr * (1+monthlyIntr)**terms) / ((1+monthlyIntr)**terms-1)#(apr/12) * (1/1-(1+apr/12) ** terms ) * principle
	
if __name__ == '__main__':
#	print(getMortgagePayment(250000, .15, 15*12)) #Yay verified to be correct! :D
#	print(getMortgagePayment(250000, .07, 25*12)) #Yay verified to be correct! :D
	print("Enter your total loan:")
	p = int(sys.stdin.readline())
	print("Enter your apr (between 0 and 1):")
	a = float(sys.stdin.readline())
	print("Enter your loan terms (number of months):")
	t = int(sys.stdin.readline())
	
	print("Your monthly payment is: " + str(getMortgagePayment(p, a, t) ) )
	