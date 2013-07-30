# Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

import sys

def rectarea(width, length):
	"""
	Returns the area of a square segment given two
	measurements
	"""
	return width*length
def cost(surfaceArea, costPerUnit):
	"""
	Returns the cost of covering an area by the cost per square 
	unit of material to cover the floor with.
	"""
	return surfaceArea * costPerUnit
	
if __name__ == '__main__':
	print("Enter the cost per unit:")
	costperunit = int(sys.stdin.readline())
	print("Enter floor width:")
	width = int(sys.stdin.readline())
	print("Enter floor length:")
	length = int(sys.stdin.readline())
	print("The total cost will be: $" + str( cost( rectarea( width, length ), costperunit ) ) ) 