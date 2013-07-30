# Enter a string and the program counts the number of vowels in the text.
#For added complexity have it report a sum of each vowel found.

import sys
import re

# Y is no strictly a vowel, but it could be if someone ordered me to do it :P
regexVowels = re.compile("[aeiouAEIOU]")

def getVowelCount(string):
	"""
	This function uses regular expression above to find all the vowels in a word
	Vowels are defined as a,e,i,o, or u. Y is not considered a vowels, but could 
	easily be added to the regular expression
	"""
	return len(regexVowels.findall(string))

if __name__ == '__main__':
#	Test code
	stringList = [ "Banana", "fox", "Elephant", "Caacleqpodx" ]
	vowelCount = [ 3, 1, 3, 4 ]
	
	for i in range(len(stringList)):
#		print( str(getVowelCount(stringList[i]) ) ) 
		assert( vowelCount[i] == getVowelCount(stringList[i]) )
	input = sys.stdin.readline()
	print("The number of vowels in \'" + input + "\' is " + str( getVowelCount(input) ) )
#	print("Success!")
