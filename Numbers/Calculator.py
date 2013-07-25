"""
Calculator program which implements basic operators
Implemented operators: Addition, subtraction, multiplication, division and exponentiation

Reimplemented the operators for fun

Only implements the implemented operators
"""
#refer to http://www.codeproject.com/Articles/24125/Parsing-Algebraic-Expressions-Using-the-Interprete
#A simple calculator to do basic operators.
#Make it a scientific calculator for added complexity.
#Stretch Goal: Add in syntax tree for basic algebra operators, will do in Classes section
# Developed for Python 3.3
import sys	#import system things
import ast  # Abstract Syntax Tree
import re
#addition implementation
def add(opa, opb):
	return opa + opb

#subtraction implementation
def sub(opa, opb):
	return opa - opb
	
#multiplication implementation
def mul(opa, opb):
	result = 0
	if(opb >=0):
		for i in range(opb):
			result += opa
	else:
		for i in range(-opb):
			result -= opa
	return result
	
#division implementation, simple
def div(opa, opb):
	quo = 0
	if(opb != 0):
		while(opa >= opb):
			opa-=opb
			quo += 1
		rem = opa
	else:
		raise DivideByZeroError("Silly person, you divided by 0")
	return quo, rem
	
def exp(opa, opb):
	result = 1
	#if operand b is greater than 0
	if(opb >= 0):
		for i in range(opb):
			result = result * opa
	#otherwise by definition it's less than 0
	else:
		for i in range(opb):
			result = result / opa
	return result
	

def calc(expression):
	print("Expression to parse: " + expression)
	expression = expression.split(' ')
	if( expression[1] == '+'):
		return add(int(expression[0]), int(expression[2]))
	elif( expression[1] == '-'):
		return sub(int(expression[0]), int(expression[2]))
	elif( expression[1] == '*'):
		return mul(int(expression[0]), int(expression[2]))
	elif( expression[1] == '/'):
		return div(int(expression[0]), int(expression[2]))
	elif( expression[1] == '^'):
		return exp(int(expression[0]), int(expression[2]))
	else:
		raise SyntaxError("Unknown operator or too many operators")
if __name__ == '__main__':
	#Debug code
#	assert(10 == add(5,5))
#	assert(0 == sub(5,5))
#	assert(-25 == mul(-5, 5))
#	assert(-25 == mul(5, -5))
#	assert(0  == mul(5, 0))
#	assert(25 == mul(5, 5))
#	assert( (5, 0) == div(25, 5) )
#	assert( (4, 3) == div(23, 5) )
	#assert( [0, 0] == div(25, 0) )
#	print(calc("1 + 3"))
#	print(calc("1 - 3"))
#	print(calc("1 * 3"))
#	print(calc("1 / 3"))
#	print(calc("1 ^ 3"))
	run = True
	while(run):
		print("Please enter equation to parse")
		print("Keep a space between operator and operands")
		print("Use the following syntax when writing your equations:")
		print("+:addition")
		print("-:subtration")
		print("*:multiplication")
		print("/:division")
		print("^:exponent")
		print(calc(sys.stdin.readline())) #enter in number and print result