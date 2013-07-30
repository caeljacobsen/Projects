# Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
# Developed for Python 3.3
import sys
import re
"""
Simple binary to decimal and back converter
"""
#takes a integer
def decToBin(dec):
	"""
	Converts dec into a string representing a binary number.
	"""
	#Ensuring clean input
	dec = int(dec)
	bin = ""
	while dec > 0:
		# Determine if it is a binary value. If it is greater than something.
		bin += (str(dec % 2))
		#go to next one.
		dec = dec // 2	#force integer division
	bin = bin[::-1] # Extended slice syntax, pretty much boss.
	return bin
	
#takes string representation of a number
def binToDec(binary):
	"""
	Returns a decimal value when given a binary number string.
	"""
	#Ensuring clean input
	#print(binary)
	#print(int(binary))
	#binary = bin(int(binary))
	binary = re.match("[01]+", binary).group(0)
	print(binary)
	dec = 0
	#reverse the string to properly 
	binary = str(binary)
	binary = binary[::-1]
	#print(binary)
	for i in range(len(binary)) :
		#Add each bits value to dec
		#bit value is (bit ** i)
		dec = dec + (int(binary[i]) * (2 ** i))
		print(str(binary[i]) + "," + str(i) +"," + str(dec))
		#print(str(dec))
	return dec	
	
if __name__ == '__main__':
	number = re.compile("[0-9]+")
	while(True):
		print("Select conversion type")
		print("1: Decimal to Binary")
		print("2: Binary to Decimal")
		#print("3: Binary to Hex")
		#print("4: Decimal to Hex")
		option = sys.stdin.readline()
		if(int(option) > 5 or int(option) < 1):
			continue
		print()
		print("Enter number to convert")
		input = sys.stdin.readline()
		if(number.match(input) != None):
			if int(option) == 1:
				print(input + " as binary is " + decToBin(input))
			elif int(option) == 2:
				print(input + " as decimal is " + str(binToDec(input)))
		else:
			print("Bad input")