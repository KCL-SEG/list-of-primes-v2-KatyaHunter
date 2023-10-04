"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
	list = []
	possPrime = 2
	numPrimesFound = 0
	isPrime = True

	if number_of_primes <= 0:
		raise ValueError("The value of number of primes cannot be 0 or negative")

	while numPrimesFound != number_of_primes:
		isPrime = True
	
		if possPrime == 2:
			isPrime = True
		
		else:
			for i in range (2, possPrime):
				if possPrime % i ==0:
					isPrime = False

		if isPrime == True:
			list.append(possPrime)
			numPrimesFound += 1

		possPrime += 1

	return list




