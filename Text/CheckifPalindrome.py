# Checks if the string entered by the user is a palindrome.
#That is that it reads the same forwards as backwards like racecar

import sys

def checkPalindrome(string):
	"""
	Takes any string of any size, if the string is the 
	same forwards as it is backwards, it is a palindrome.
	"""
	string = string.lower()
	#May modify to utilize regular expressions in the future to make a much more powerful palindrome checker. This works for now, though.
	string = string.replace(' ', '') 
	if(string == string[::-1]):
		return True
	else:
		return False

if __name__ == '__main__':
	assert(checkPalindrome("Racecar") == True)
	assert(checkPalindrome("Banana") == False)
	assert(checkPalindrome("Hannah") == True)
	assert(checkPalindrome("Madam Im Adam") == True)
	assert(checkPalindrome("Racecar Hannah Anna Hannah Racecar") == True)
	print("Success!")