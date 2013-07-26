# Asks the user to enter a cost and either a country or state tax.
#It then returns the tax plus the total cost with tax.

import sys

def getSalesTax(cost, tax):
	return round(cost * tax,2)

if __name__ == '__main__':
	print("Input cost of transaction:")
	cost = float(sys.stdin.readline())
	
	print("Input sales tax percentage:")
	tax = float(sys.stdin.readline())
	tax = getSalesTax(cost, tax)
	print("Tax: " + str(tax))
	
	print("Total: " + str(tax+cost))