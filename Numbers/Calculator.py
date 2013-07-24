#A simple calculator to do basic operators.
#Make it a scientific calculator for added complexity.
import sys	#import system things
import ast	#import syntax tree code
#addition implementation
def add(opa, opb):
	return opa+opb
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
	#definition of exponents
	if( opb == 0 ):
		return 1
	else:
		#if operand b is greater than 0
		if(opb > 0):
			for i in range(opb):
				opa *= opa
		#otherwise by definition it's less than 0
		else:
			for i in range(opb):
				opa / opb
	return opa
	
#parses 
def eqParser(equation):
	#Use pythons compiler/parser to create the syntax tree
	return equation
	
def calc(synTree):
	print(synTree)
#Debug code
if(False):
	assert(10 == add(5,5))
	assert(0 == sub(5,5))
	assert(-25 == mul(-5, 5))
	assert(-25 == mul(5, -5))
	assert(0  == mul(5, 0))
	assert(25 == mul(5, 5))
	assert( (5, 0) == div(25, 5) )
	assert( (4, 3) == div(23, 5) )
	#assert( [0, 0] == div(25, 0) )
else:
	run = True
	while(run):
		print("Please enter equation to parse")
		print("Use the following syntax when writing your equations:")
		print("+:addition")
		print("-:subtration")
		print("*:multiplication")
		print("/:division")
		print("**:exponent")
		print("(): Parenthesis")
		calc(eqParser( sys.stdin.readline() ))