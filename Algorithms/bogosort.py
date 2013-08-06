from sys import argv
import argparse
import random
array = argv[1]
array = array.split(",")
array = [int(l) for l in array] 

def isSorted(array = []):
	n = 1
	while( n < len(array)-1 ):
		if( array[n] < array[n-1] ):
			return False
		n = n + 1
	return True
	
def shuffle(array = []):
	temp = 0
	rand = 0
	for i in range( len(array) ):
		temp = array[i]
		rand = int( random.random() * ( len(array)-1 ) )
		array[i] = array[rand]
		array[rand] = temp
	return array
	
def bogosort(array = []):
	while(not isSorted(array)):
		array = shuffle(array)
		print("Shuffle!" + str(array) )
	return array

print("Acquired array: " + str(array) )
print("Bogo sort activate!")
array = bogosort(array)
print("Bogo sort complete!")
print(array)