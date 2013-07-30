# Counts the number of individual words in a string.
#For added complexity read these strings in from a text file and generate a summary.

import sys

def getWordCount(string):
	"""
	Function used to get the number of words in a string. A word is delimited by spaces. 
	The string parameter should be a single line string. Two calls would be required for multiple lines
	Words with any other punctuation are treated as a whole word until the next space is seen
	"""
	list = string.split(' ') #spaces denote separation between words
	return len(list)

def readFile(filename):
	"""
	Function used to open and read a file specified by the user and count the words in the file.
	"""
	wordCount = 0
	try:
		print(filename)
		filename = filename.replace('\n', '') #Clear out extra line feeds if there
		file = open(filename)
		for line in file:		
			wordCount += getWordCount(line)	
	except IOError as err:
		print("I/O error: {0}".format(err))
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