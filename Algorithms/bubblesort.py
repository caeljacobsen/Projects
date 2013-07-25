from sys import argv
import argparse

array = argv[1]
print array
array = array.split(",")
print array

def properbubblesort(array = []):
	while True:
		swapped = False
		for index in range(len(array)-1):
			if(int(array[index]) > int(array[index+1])):
				print "SWAP!", index, index + 1
				temp = array[index]
				array[index] = array[index+1]
				array[index+1] = temp
				swapped = True
			print array
		if(not swapped):
			break
	return array	
				

def superiorbubblesort(array = []):
	index = 0
	while index < len(array)-1:
#		print index, array[index], array[index+1]
		if(int(array[index]) > int(array[index+1])):
			print "SWAP!", index, index + 1
			temp = array[index+1]
			array[index+1] = array[index]
			array[index] = temp
			index -= 1 
			if(index < 0):
				index = 1
		#	print array
		else:
			index += 1
		print array
	return array
print "Acquired array:", array
print "Bubble sort activate!"
array = superiorbubblesort(array)
print "Bubble sort complete!"
print array