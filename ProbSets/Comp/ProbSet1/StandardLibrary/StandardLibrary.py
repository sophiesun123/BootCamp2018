# STANDARD LIBRARY

# function that returns the min, max, and average
def sl1(list):
	print(min(list), max(list), sum(list)/len(list))

# function that returns whether or not an int is mutable
def i():
	x = 4
	y = x
	x += 2
	if y == x:
		print("ints are mutable")
	else:
		print ("ints are immutable")

# function that returns whether or not a string is mutable
def s():
	x = "hi"
	y = x
	x = "bye"
	if y == x: 
		print("strings are mutable")
	else:
		print ("strings are immutable")

# function that returns whether or not a list is mutable
def l():
	x = [0, 2, 3]
	y = x
	x[0] = 1
	if y == x: 
		print("lists are mutable")
	else:
		print ("lists are immutable")

# function that returns whether or not a tuple is mutable
def t():
	x = (0, 1)
	y = x
	x += (1,)
	if y == x: 
		print("tuples are mutable")
	else:
		print ("tuples are immutable")

# function that returns whether or not a set is mutable
def se():
	x = set([1, 2, 3])
	y = x
	x.add(4)
	if y == x: 
		print("sets are mutable")
	else:
		print ("sets are immutable")

# function that returns the length of the hypotenuse
import calculator as calc
from math import sqrt
def sl3(a, b):
	sqrt(add(mult(a, a), mult(b, b)))

# function that computes the power set of a set
from itertools import combinations
def sl4(a): 
	lst = []
	for i in range(len(a) + 1):
		# finds all combinations of all lengths
		for combos in combinations(a, i):
			lst.append(set(combos))
	print(lst)

