#!/usr/bin/env python
import sys

# Input: non-negative integers a, b 
# Output: (a / b), the Jacobi symbol of a w.r.t. b
def jacobi(a, b):

	print("Jacobi({}, {})".format(a, b))
	if a == 1 or a == 0:
		print(" = {}".format(a))
		return a

	if a % 2 != 0:

		if a % 4 == 3 and b % 4 == 3:
			print(" = -Jacobi({} mod {}, {})".format(b, a, a))
			return -jacobi(b % a, a) 
		else: 
			print(" = Jacobi({} mod {}, {})".format(b, a, a))
			return jacobi(b % a, a)

	else:
		
		if b % 8 == 1 or b % 8 == 7:
			print(" = Jacobi({} / 2, {})".format(a, b))
			return jacobi(a/2, b)
		else:
			print(" = -Jacobi({} / 2, {})".format(a,b))
			return -jacobi(a/2, b)


a = int(sys.argv[1])
b = int(sys.argv[2])
print("\nJacobi({}, {}) = {}".format(a, b, jacobi(a,b)))
