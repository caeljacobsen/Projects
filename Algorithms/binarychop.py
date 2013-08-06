from sys import argv
import argparse

number = argv[1]
array = argv[2]
print array
array = array.split(",")
print array

def chop(numToFind, arrayToSearch = [], offset = 0):
	lowerBound = 0
	upperBound = len(arrayToSearch)
	if(int(upperBound) > int(lowerBound+1)):
		index = (lowerBound+upperBound)/2
		print(lowerBound + " " + upperBound + " " + index)
	else:
		return -1
	if(int(numToFind) == int(arrayToSearch[index])):
		print("FINAL CHOP!")
		return index+offset
	elif(int(numToFind) > int(arrayToSearch[index])):
		print("HIGH CHOP!")
		return chop(numToFind, arrayToSearch[index:], index+offset)
	elif(int(numToFind) < int(arrayToSearch[index])):
		print("LOW CHOP!")
		return chop(numToFind, arrayToSearch[:index], offset)
	else:
		return -1

print("Starting katachop!")
print("KATACHOP " + number + " FROM " + array + "!")
index = chop(number, array, 0)
if(index < 0):
	print( "Index does not exist, shishou!")
else:
	print( "Here is your index, shishou! " + index)