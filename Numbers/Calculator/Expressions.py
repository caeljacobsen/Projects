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
import abc

#Expression Base Class
@abc.abstractbaseclass
class Expression(metaclass=ABCMeta):
	def __init__(self):
		self.ZERO_THRESHOLD = 1.0 * (10 ** -14)
		bool(self.isBound)
		self.isBound = False
	
	def Bind(self, args):
		InnerBind(args):
		self.isBound = True
		
	def Evaluate(context):
		result = InnerEvaluate(context)
		
		if( abs(result) <= self.ZERO_THRESHOLD):
			return 0
		else
			return result
	@abstractmethod
	def InnerBind(self, args):
		raise NotImplementedError
	@abstractmethod
	def InnerEvaluate(self, context):
		raise NotImplementedError
	
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
	