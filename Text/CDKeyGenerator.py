# Generates a unique key for your applications to use based on some arbitrary algorithm that you can specify.
#Great for software developers looking to make shareware that can be activated.

import sys
import datetime
import hashlib
import base64

#Assumption for CD key dispersal being account login on server to purchase software
#Allows recovery and other options with current CD key scheme

#Reseller is the plaintext ID given to each different 
#date time is the current date 
def generateSerialKey(resellerId, productNumber, batch, number):
	""" 
	This function takes a Merchant's ResellerID, the product number, batch number and unit number and 
	Returns a unique serial key from it using the date.
	"""
	date = datetime.date.isoformat(datetime.date.today()).replace("-", "")
	serialKey = date + "-" + resellerId + "-" + productNumber + "-" + batch + "-" + number
	return serialKey

#Returns base 64 hashed string. formatted appropriately for a CD Key
def hashSerial(serialKey):
	"""
	This function takes a unique serial key and runs it through 
	a hashing function to secure and hide the actual serial information. 
	Returns the hashed version of the serial key code.
	"""
	formatSpacing = 10	#magic formatting number!
	hash = hashlib.sha1()	#Good enough for my uses now to get a shortish key
							#Revisit with a better algorithm to get a shortish key
	hash.update( str(serialKey).encode("utf-8") ) #, "utf-8") )
	digest = hash.hexdigest()
	digest = digest.upper()
	#make string more readablish
	for i in range(len(digest) + len(digest)//formatSpacing):
		if( i > 0 and i % formatSpacing == 0):
			digest = digest[:i-1] + '-' + digest[i-1:]	
	return digest
	
	
if __name__ == '__main__':
	assert(	datetime.date.isoformat(datetime.date.today()).replace("-", "") + "-" +
			"12345" + "-" +  "8732" + "-" + "00010" + "-" + "1523" == 
			generateSerialKey("12345", "8732", "00010", "1523") )
	print(	generateSerialKey("12345", "8732", "00010", "1523")	)
	print(	hashSerial( generateSerialKey( "12345", "00010", "8732" , "1523" ) ) )
	print( "Success" )