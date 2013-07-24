#	Python script to set up each directory
import os
import os.path
import re
import sys
import codecs

lineDelim = '-'
filenameRegex = "([\*\*])|([/])|(\s)"
filecommentRegex = "([\.\s]|"
#Creates the base file
#name is the name of the file to create without the suffix
#description is the description of the project to make
def createFile(name,  desc):
	file = open(name , 'w')
	file.write("#" + desc)
	file.flush()
	file.close()
	
def parseFile(filename):
	if(os.path.exists(filename)):
		print("Opening project list: " + filename)
		file = open(filename, 'r')
		nameRegex = re.compile(filenameRegex)
		while(True):
			line = file.readline()
			if(line == ""):
				break
			elif(nameRegex.match(line) == None or line == '\n'):
				continue
			else:
				line = line.split(lineDelim)
				#print(line)
				name = nameRegex.subn("", line[0]) 
				name = name[0]
				name += ".py"
				print(name)
				comment = line[1].replace(". ", ".\n#")
				createFile(name, comment)
	else:
		print("No project list")
		
print("Starting setup process")
#os.chdir(os.path.dirname(sys.argv[0]))
#os.chdir("D:\Dev\Projects\Personal\Python Projects")
print(os.getcwd())
for d in os.listdir(os.curdir):
	print(os.path.abspath(d))
	if(os.path.isdir(d)):
		print("In directory:" + d)
		os.chdir(d)
		print("Reading project list")
		parseFile("README.md")
		os.chdir("..")
	else:
		print("Not a directory")