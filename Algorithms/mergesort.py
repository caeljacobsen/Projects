from sys import argv
import argparse

array = argv[1]
array = array.split(",")
array = [int(l) for l in array] 

def merge(left = [], right = []):
	result = []
	while len(left) > 0 or len(right) > 0:
		if len(left) > 0 and len(right) > 0:
			if left[0] <= right[0]:
				result.append(left[0])
				left = left[1:]
			else:
				result.append(right[0])
				right = right[1:]
		elif len(left) > 0:
			result.append(left[0])
			left = left[1:]
		elif len(right) > 0:
			result.append(right[0])
			right = right[1:]
	return result
	
	
def mergesort(array = []):
#	print array
	if len(array) <= 1:
		return array
	midpoint = len(array)/2
	left = array[:midpoint]
	right = array[midpoint:]
	left = mergesort(left)
	right = mergesort(right)
	print left, right
	return merge(left, right)

print "Acquired array:", array
print "Merge sort activate!"
array = mergesort(array)
print "Merge sort complete!"
print array