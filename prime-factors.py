#!/usr/bin/env python
import sys
import math

# Input: integer a > 1 
# Output: a list of all prime numbers 1 through a 
def sieve(a):

	A = [True] * a
	for i in range(2, int(math.sqrt(a))+1):
		if A[i] == True:
			 for j in range(i**2, a, i):
				A[j] = False

	return [p for p in range(2, a) if A[p] == True]

# Input: integer a > 1
# Output: a list of all prime factors of a, if they exist
def prime_factors(n):
	factors = []
	for p in sieve(n):
		if (n % p == 0):
			factors.append(p)
	return factors


a = int(sys.argv[1])
print("\nprime factors({}) = {}".format(a, prime_factors(a)))


