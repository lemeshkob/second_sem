import sys
import math




def row(n):
	print("\n Row: \n 1/2 + 2/2^2 + 3/2^3 + ... + n/2^n + ...")
	n = float(n)
	score = ((n/2 ** n) ** 1/n)

	if score < 1:
		print("Good")
	else:
		print("Not good")
