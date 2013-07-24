"""
Takes a string and turns it into expression tokens.
"""
#refer to http://www.codeproject.com/Articles/24125/Parsing-Algebraic-Expressions-Using-the-Interprete
#A simple calculator to do basic operators.
#Make it a scientific calculator for added complexity.
#Stretch Goal: Add in syntax tree for basic algebra operators

import sys	#import system things
import re

tokenPattern = re.compile("\s*(?:(\d+)|(.))")

def tokenize(program):
	for number, operator in token_pattern.findall(

class LiteralToken(object):
	def __init__(self, value):
		self.value = int(value)
	def nud(self):
		return self.value
class operator_add_token(LiteralToken):
	leftBindingPower = 10
	def leftDenotation(self, left):
		right = expression(10)
		return left + right