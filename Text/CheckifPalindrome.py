# Checks if the string entered by the user is a palindrome.
#That is that it reads the same forwards as backwards like racecar

import sys

def checkPalindrome(string):
	string = string.lower()
	if(string == string[::-1]):
		return True
	else:
		return False

if __name__ == '__main__':
	assert(checkPalindrome("Racecar") == True)
	assert(checkPalindrome("Banana") == False)
	assert(checkPalindrome("Hannah") == True)
	print("Success!")