# Counts the number of individual words in a string.
#For added complexity read these strings in from a text file and generate a summary.

import sys

def getWordCount(string):
	list = string.split(' ') #spaces denote separation between words
	return len(list)

if __name__ == '__main__':
#	Test code
	assert(getWordCount("This has four words!") == 4)
	assert(getWordCount("I am a banana man!") == 5)
	assert(getWordCount("Words, words. They're all we have to go on.") == 9)
	print("Success!")