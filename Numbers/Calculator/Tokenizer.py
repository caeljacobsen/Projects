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

#Tokenizer class
class Tokenizer(object):
	raise NotImplementedError