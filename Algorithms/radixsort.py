from sys import argv
import argparse
from collections import deque
import math
array = argv[1]
#base = int(argv[2])
array = array.split(",")
array = [int(l) for l in array] 

def radixsort(array, base = 10):
	# Check if the array is sorted
	# Create 10 queues, one for each digit.
	queueList = []
	for i in range(10):
		queueList.append(deque())
	
	# Find the largest number in the list.
	highestNumber = max( abs(num) for num in array )
	#Acquire the total number of passes in the algorithm (1 for each digit)
	totalPasses = int(math.log(highestNumber, base) + 1)
	for digitNum in range(totalPasses):
		#print(digitNum)
		print(array)
		for num in array:
			index = str(num).zfill(digitNum + 1)
			index = index[::-1]
			#print("Value: " + str(index) + " Digit: " + str(digitNum) + " index[digit]:" + str(index[digitNum]) )
			#print(digitNum)
			#print(index[digitNum])
			queueList[int(index[digitNum])].appendleft(num)
		#print(str(queueList))
		array = []
		for q in queueList:
			while(len(q) > 0):
				array.append(q.pop())
	
	# Return the sorted array
	return array
print("Acquired array: " + str(array))
print("Radix sort activate!")
array = radixsort(array)
print("Radix sort complete!")
print(array)