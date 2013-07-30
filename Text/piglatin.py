# Pig Latin is a game of alterations played on the English language game.
# To create the Pig Latin form of an English word the initial consonant sound 
# is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield ananabay)

import re
#Covers standard consonants, common digraphs and common trigraphs
wordstart = "((chr|ch|gh|gn|ll|ph|qu|sh|th|wh|wr)|[b-df-hj-np-tv-zB-DF-H-J-NP-TV-Z])"
wordend = wordstart + "(ay)"

def encodePiglatin(string):
	"""
	Accepts a single word in english 
	returns the corresponding lower case piglatin word
	"""
	string = string.lower()
	consonant = re.compile(wordstart)
	piglatin = consonant.match(string)		# Find the first consonant
	piglatin = piglatin.group(0).lower() + "ay"
	piglatin = consonant.sub("", string, 1) + piglatin 	# Remove the first consonant you see
	return piglatin.lower()

def decodePiglatin(string):
	"""
	Accepts a single word in piglatin 
	Returns the corresponding english word.
	"""
	string = string.lower()
	suffix = re.compile(wordend) 
	piglatin = suffix.search(string)#string[len(string)-3:])
	piglatin = piglatin.group(0)		#Get the full substring
	piglatin = piglatin.replace("ay","")	#Linguistic portion, always has the two letter 'ay'  tacked onto the end of it. Eliminate them >:|
	english = suffix.subn("", string)[0]	#use the regex to sub that portion of the word off.
	english = piglatin + english	
	return english.lower()
	
if __name__ == '__main__':
	#Test cases
	assert( encodePiglatin("Banana") == "ananabay" )
	assert( encodePiglatin("BanAna") == "ananabay" )
	assert( encodePiglatin("BaNAna") == "ananabay" )
	assert( encodePiglatin("BANANA") == "ananabay" )
	assert( decodePiglatin("Ananabay") == "banana" )
	assert( decodePiglatin("AnanABay") == "banana" )
	assert( decodePiglatin("AnanaBAY") == "banana" )
	assert( decodePiglatin("ANANABAY") == "banana" )
	assert( encodePiglatin("Theorem") == "eoremthay" )
	assert( encodePiglatin("THEorem") == "eoremthay" )
	assert( encodePiglatin("TheOREM") == "eoremthay" )
	assert( decodePiglatin("EoreMThay") == "theorem" )
	assert( decodePiglatin("EoremTHAY") == "theorem" )
	assert( decodePiglatin("Eoremthay") == "theorem" )
	assert( encodePiglatin("Chrome") == "omechray" )
	assert( decodePiglatin("Omechray") == "chrome" )
	print("Success!")