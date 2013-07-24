"""
Calculator program which implements basic operators
Implemented operators: Addition, subtraction, multiplication, division and exponentiation

Also includes a basic algebra parser creating syntax trees for simple 
algebraic operands. 

Only implements the implemented operators
"""
#refer to http://www.codeproject.com/Articles/24125/Parsing-Algebraic-Expressions-Using-the-Interprete
#A simple calculator to do basic operators.
#Make it a scientific calculator for added complexity.
#Stretch Goal: Add in syntax tree for basic algebra operators

import sys	#import system things
import ast  # Abstract Syntax Tree


def calc(synTree):
	print(synTree)
	
if __name__ == '__main__':
	#Debug code
	assert(10 == add(5,5))
	assert(0 == sub(5,5))
	assert(-25 == mul(-5, 5))
	assert(-25 == mul(5, -5))
	assert(0  == mul(5, 0))
	assert(25 == mul(5, 5))
	assert( (5, 0) == div(25, 5) )
	assert( (4, 3) == div(23, 5) )
	#assert( [0, 0] == div(25, 0) )
#	calc(eqParser( "( 1 + 3 * (4 - 1) ) / 5 "))
	#run = True
	#while(run):
	#	print("Please enter equation to parse")
	#	print("Use the following syntax when writing your equations:")
	#	print("+:addition")
	#	print("-:subtration")
	#	print("*:multiplication")
	#	print("/:division")
	#	print("**:exponent")
	#	print("(): Parenthesis")
	#	calc(eqParser( sys.stdin.readline() ))