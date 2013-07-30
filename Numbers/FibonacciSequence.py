# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
import sys

def fibonacci(n):
	"""
	Gets returns the nth number in the fibonacci sequence
	"""
	last = 0
	number = 1
	deg = 0
	while(deg < n):
		temp = number
		number = last + number
		last = temp
		deg += 1
	return number

if __name__ == '__main__':
	print("Enter the nth degree of the Fibonacci to generate:")
	degree = int(sys.stdin.readline())
	print("The fibonacci number at " + str(degree) + " is " + str(fibonacci(degree)))