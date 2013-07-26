# Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) 
# and validates it to make sure that it is a valid number (look into how credit cards use a checksum).

import sys

#Luhn Checksum, uses industry standard checksum to validate it
#takes string
#returns 1 if valid, 0 if not
def creditCardValidate(cardNumber):
	sum = 0
	oddOrEven = len(cardNumber) & 1
	
	for i in range(len(cardNumber)):
		digit = int(cardNumber[i])
		
		if not ( ( i & 1 ) ^ oddOrEven ) :
			digit = digit * 2
		if digit > 9 :
			digit = digit - 9
		sum = sum + digit
	return ( (sum % 10) == 0 )
	
if __name__ == '__main__':
	#running test credit card numbers
	#american express
	assert( 1 == creditCardValidate("378282246310005") )
	#discover
	assert( 1 == creditCardValidate("6011111111111117") )
	#mastercard
	assert( 1 == creditCardValidate("5555555555554444") )
	#visa
	assert( 1 == creditCardValidate("4111111111111111") )
	print("Test Complete - All pass")