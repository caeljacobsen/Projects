# Counts the number of individual words in a string.
#For added complexity read these strings in from a text file and generate a summary.

import sys

def getWordCount(string):
	list = string.split(' ') #spaces denote separation between words
	return len(list)

def readFile(filename):
	wordCount = 0
	file = open(filename)
	for line in file:		
		wordCount += getWordCount(line)	
	return wordCount
	
if __name__ == '__main__':
#	Test code
#	assert(getWordCount("This has four words!") == 4)
#	assert(getWordCount("I am a banana man!") == 5)
#	assert(getWordCount("Words, words. They're all we have to go on.") == 9)
#	print("Success!")
	print("Enter file name to count the words for")
	file = sys.stdin.readline()
	print("Attempting to open the file: " + file)
	print( "Number of words: " + str( readFile(file) ) ) 