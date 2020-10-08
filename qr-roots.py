#!/usr/bin/env python
import sys

# Input: Prime p, integer a in QR_p, integer b in QNR_p
# Output: A candidate square roots of a (only one will make sense)

def alg(p, a, b):

	if p % 4 == 3:
		return pow(a, (p+1)/4, p)  
	else:
		r = (p - 1)/2
		r_0 = 0
		
		while r % 2 == 0:

			# maintain invariant a**r b**r_0 = 1 % p
			r = r / 2
			r_0 = r_0 / 2

			# the below is a more efficient way to compute
			# if a**r*b**r_0 == p-1 % p
			# for large numbers
			mod1 = pow(a, r , p) 
			mod2 = pow(b, r_0, p)
			if mod1*mod2 % p == (p-1):
				r_0 += (p-1)/2

		mod1 = pow(a, (r+1)/2 , p) 
		mod2 = pow(b, r_0/2, p)
		ans = mod1*mod2 % p
		return ans, ans - p		



p = int(sys.argv[1])
a = int(sys.argv[2])
b = int(sys.argv[3])
print("\nSquare root {} modulo prime {}: +/- {}".format(a, p, alg(p,a,b)))
