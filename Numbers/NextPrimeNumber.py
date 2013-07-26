# Have the program find prime numbers until the user chooses to stop asking for the next one.
testPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

#Returns a list of n primes all that are found
#Uses concept that a prime is a number than is not divisible by any other prime.
from math import sqrt
def getNPrime(n):
	primesList = [2] # Two is a given prime
	numberToTest = 3 # Three is the next number to test
	while(len(primesList) < n):
		isPrime = True
		# check all numbers in the primes list so far
		for divisor in primesList:
			#module operation, if it divides perfectly or moduluses it isn't prime
			if numberToTest % divisor == 0:
				isPrime = False
				break
			#if it gets to the square root, all base factors have been attempted
			# Exponentiation is faster than square rooting, I think
			if divisor ** 2 > numberToTest:
				break
				
			# if it passed the test then put it on the list, yay!
		if isPrime:
			primesList.append(numberToTest)
		numberToTest = numberToTest + 1
	return primesList	

#Same as above but uses generators instead
def genNPrimes():	
	primesList = [2] # Two is a given prime
	yield(2)
	numberToTest = 3 # Three is the next number to test
	#Since it's a generator there is no need to set an upper limit. It's up to the user to do that
	while(True):
		isPrime = True
		# check all numbers in the primes list so far
		for divisor in primesList:
			#module operation, if it divides perfectly or moduluses it isn't prime
			if numberToTest % divisor == 0:
				isPrime = False
				break
			#if it gets to the square root, all base factors have been attempted
			# Exponentiation is faster than square rooting, I think
			if divisor ** 2 > numberToTest:
				break
				
			# if it passed the test then put it on the list, yay!
		if isPrime:
			primesList.append(numberToTest)
			yield(numberToTest)
		numberToTest = numberToTest + 1
	return primesList
if __name__ == '__main__':
	print(getNPrime(50))
	assert(testPrimes == getNPrime(168))
#	print(getNPrime(100000))
	primes = genNPrimes()
	for p in primes:
		print(p)
	print("Success!")