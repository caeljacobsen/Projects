# Enter a number and have the program generate PI up to that many decimal places.
#Keep a limit to how far the program will go.
import sys

# arccot(x) = 1/x - 1/(3x^3) + 1/(5x^5) - 1/(7x^7)
#Taylor series implementation
def arccot(x, taylorPrecision):
	"""
	Calculates the arc cotangent of using the taylor series, model.
	Returns the value of the cotangent based upon X
	"""
	sum = expPower = taylorPrecision // x
	n = 3
	sign = -1
	while True:
		expPower = expPower // (x*x) # integer division 3 = 
		term = expPower // n	
		if not term:
			break
		sum += sign * term #Add next value to taylor series
		sign = -sign #changes to opposite sign
		n += 2 #next term value
	return sum
			
#Uses Machin's Formula
# Pi/4 == 4 arccot 5 - arccot 239
def getPI(precision = 10):
	"""
	Returns the digits of PI to the desired precision with a default of 10 significant digits.
	Return type is string
	"""
	taylorPrecision = 10 ** (precision + 10)
	#pi = 4* (4 arccot 5 - arccot 239)
	pi = 4 * (4*arccot(5, taylorPrecision) - arccot(239, taylorPrecision))
	return pi
	
def getStrPI(precision = 10):
	"""
	Helper function to get pretty printed pi rather than simply PI digits
	"""
	return "3." + str(getPI(precision))[1:]
	
if __name__ == '__main__':
	
	print(getStrPI(10))
	print("")
	print(getStrPI(100))
	print("")
	print(getStrPI(1000))
	print("")
	print(getStrPI(10000))
	print("")
	
	print("Test Complete and successful")