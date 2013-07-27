# Enter a string and the program will reverse it and print it out.

import sys

#Normally wouldn't make my own method because it's built in
#But why not? xD
def manReverse(string):
	newStr = ""
	# iterate backwards through the string
	for i in range(len(string), 0 , -1):
		newStr += string[i-1] #For proper indexing purposes
	return newStr

if __name__ == '__main__':
	string = sys.stdin.readline()
	print(string[::-1])	#extended slice syntax is amazing like that
	print(manReverse(string))