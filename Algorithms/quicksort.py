from sys import argv
import argparse

array = argv[1]
array = array.split(",")
array = [int(l) for l in array] 
def quicksort(array = []):
	if len(array) <= 1 :
		return array
#	print array
	pivotIndex = len(array)/2
	pivotValue = array.pop(pivotIndex)
	less = []
	greater = []
	for i in range(len(array)):
		if int(array[i]) <= int(pivotValue):
			less.append(array[i])
		else:
			greater.append(array[i])
#	print less, "  ", pivotValue, " ", greater
	return (quicksort(less) + [pivotValue] + quicksort(greater))

print "Acquired array:", array
print "Quick sort activate!"
array = quicksort(array)
print "Quick sort complete!"
print array