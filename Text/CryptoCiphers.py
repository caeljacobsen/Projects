# Functions for encrypting and decrypting data messages.
# Then send them to a friend.
import sys
import re

def vigenereEncrypt(key, plaintext):
	"""
	Encrypts a plaintext string using Vigenere's Encryption Cipher with the associated key
	If the string contains anything other than the letters of the english alphabet, it will raise a ValueError
	Returns an encrypted utf-8 string.
	"""
	if(re.match("^[a-zA-Z]+$", plaintext) == None):
		raise ValueError("Does not accept Only accepts information from A-Z")
	ciphertext = bytearray("", "utf-8")
	key = bytearray(key.upper(), "utf-8")
	plaintext = bytearray(plaintext.upper(), "utf-8") #capitalize the word for the sake of processing
	for i in range( len( plaintext ) ) :
		#Use the algebraic representation of the Vignere cipher C[i] = (P[i] + K[i]) % 26
		#Simplification to equation
		# start: 	(p[i] - 65 + k[i] - 65) % 26 + 65
		#			(p[i] + key - 65*2) % 26 + 65
		#							65 * 2 = 130
		#							130 % 26 = 0 so it can be safetly removed from the calculation. 
		# the equation is as the code that follows.
		ciphertext.append( ( ( plaintext[i] + key[i % len(key)] ) % 26 ) + 65 )# Append the necessary value. Sub 65 to make A=0 add 65 to return it to character bit range
	
	return ciphertext.decode("utf-8")

def vigenereDecrypt(key, ciphertext):
	"""
	Decrypts a ciphertext string using Vigenere's Encryption Cipher with the associated key
	If the string contains anything other than the letters of the english alphabet, it will raise a ValueError
	Returns a plaintext utf-8 string.
	"""
	if(re.match("^[a-zA-Z]+$", ciphertext) == None):
		raise ValueError("Does not accept Only accepts information from A-Z")
	plaintext = bytearray("", "utf-8")
	key = bytearray(key.upper(), "utf-8")
	ciphertext = bytearray(ciphertext.upper(), "utf-8") #Capitalize the word for the sake of processing
	for i in range( len( ciphertext ) ) :
		# no tricky simplification here. 
		# Just  c[i] - k[i] == (c[i] - 65) - (k[i] - 65) 
		plaintext.append( ( ( ciphertext[i] - key[i % len(key)] ) % 26 ) + 65 )# Append the necessary value. Sub 65 to make A=0
	
	return plaintext.decode("utf-8")

def vernamEncrypt(key, plaintext):
	"""
	Encrypts a ciphertext string using Vernam's Encryption Cipher aka Stream Cipher with the associated key
	If the plaintext string and the key string are not exactly the same length, it will raise a ValueError
	Returns a ciphertext utf-8 string.
	"""
	if(len(key) != len(plaintext)):
		raise ValueError("Key length and text length is not the same")
	ciphertext = bytearray("", "utf-8")
	plaintext = bytearray(str(plaintext), "utf-8")
	key = bytearray(key, "utf-8")
	for i in range( len( plaintext ) ):
		ciphertext.append(plaintext[i] ^ key[i])
	
	return ciphertext.decode("utf-8")
	
def vernamDecrypt(key, ciphertext):
	"""
	Decrypts a ciphertext string using Vernam's Encryption Cipher aka Stream Cipher  with the associated key
	If the plaintext string and the key string are not exactly the same length, it will raise a ValueError
	Returns a plaintext utf-8 string.
	"""
	if( len(key) != len(ciphertext) ):
		raise ValueError("Key length and text length is not the same")
	plaintext = bytearray("", "utf-8")
	ciphertext = bytearray(str(ciphertext), "utf-8")
	key = bytearray(key, "utf-8")
	for i in range( len(ciphertext) ):
		plaintext.append(ciphertext[i] ^ key[i])
		
	return plaintext.decode("utf-8")

def caesarEncrypt(key, plaintext):
	"""
	Encrypts a plaintext string using a Caeser Shift Cipher with the associated key
	If the string contains anything other than the letters of the english alphabet, it will raise a ValueError
	Returns an encrypted utf-8 string.
	"""
	if(re.match("^[a-zA-Z]+$", plaintext) == None):
		raise ValueError("Does not accept Only accepts information from A-Z")
	ciphertext = bytearray(plaintext.upper(), "utf-8")
	for i in range( len( ciphertext ) ):
		#A = 65, remove and re-add for the math to work
		ciphertext[i] -= 65
		ciphertext[i] = ( (ciphertext[i] + key ) % 26 )
		ciphertext[i] += 65
	
	return ciphertext.decode("utf-8")
	
def caesarDecrypt(key, ciphertext):
	"""
	Decrypts a ciphertext string using Vigenere's Encryption Cipher with the associated key
	If the string contains anything other than the letters of the english alphabet, it will raise a ValueError
	Returns a plaintext utf-8 string.
	"""
	if(re.match("^[a-zA-Z]+$", ciphertext) == None):
		raise ValueError("Does not accept Only accepts information from A-Z")
	plaintext = bytearray(ciphertext.upper(), "utf-8")
	for i in range( len( plaintext ) ):
		#A = 65, remove and re-add for the math to work
		plaintext[i] -= 65
		plaintext[i] = ( (plaintext[i] - key ) % 26 )
		plaintext[i] += 65
	
	return plaintext.decode("utf-8") #return as something useful
	
if __name__ == '__main__':
	# for caeser ciphers 23 shifts right (positive) and 3 shifts left (negative) are identical
	try :
		print(caesarEncrypt(23, "A B C D E F G H I J K L "))
	except ValueError as e:
		print(type(e))
		print(str(e.args))
	assert( caesarEncrypt(23, "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "XYZABCDEFGHIJKLMNOPQRSTUVW")
	assert( caesarDecrypt(-3, "XYZABCDEFGHIJKLMNOPQRSTUVW") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	#should be able to run a plaintext through the key then the cipher text through the same key and acquire the original plaintext, albeit without spaces and in all caps.
	assert( caesarDecrypt(15, caesarEncrypt(15, "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG") )  == "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG")
	
	# test the stream cipher
	testMessage = "Encryption is a fun passtimes sometimes."
	key = "12233445567890qwertyuiopasdfghjklzxcvbnm"
	assert( vernamDecrypt( key, vernamEncrypt( key, testMessage ) ) == testMessage)
	
	#Test the vignere cipher
	print( vigenereEncrypt("LEMON", "ATTACKATDAWN"))
	assert( vigenereEncrypt("LEMON", "ATTACKATDAWN") == "LXFOPVEFRNHR" )
	assert( vigenereDecrypt("LEMON", "LXFOPVEFRNHR") == "ATTACKATDAWN" )
	print("Success!")