# Converts various units between one another.
#The user enters the type of unit being entered, the type of unit they want to convert to and then the value.
#The program will then make the conversion.

global lengthConvert 	#All length conversions are based on the meter
global tempConvert 		#All temperature conversions are based on degrees in Celsius
global 
lengthConvert = {
	'kilometer':.001
	'meter': 1, 
	'millimeter': 1000, 
	'mile':0.000621371, 
	'feet':3.28084, 
	'inches': 39.3701, 
	'nautmile': 0.000539957,
	}
