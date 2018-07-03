# UNIT TESTING

# function that returns the smallest prime factor of the positive integer n (fixed)
def smallest_factor(n):
	if n == 1: return 1
	for i in range(2, int(n ** .5) + 1):
		if n % i == 0: return i
	return n

# function that returns the number of days in the given month
def month_length(month, leap_year = False):
	if month in {"September", "April", "June", "November"}:
		return 30
	elif month in {"January", "March", "May", "July", "August", "October", "December"}:
		return 31
	if month == "February":
		if not leap_year:
			return 28
		else:
			return 29
	else:
		return None

# function that applies an arithmetic operation to a and b
def operate(a, b, oper):
	if type(oper) is not str:
		raise TypeError("oper must be a string")
	elif oper == '+':
		return a + b
	elif oper == '-':
		return a - b
	elif oper == '*':
		return a * b
	elif oper == '/':
		if b == 0:
			raise ZeroDivisionError("division by zero is undefined")
		return a / b
	raise ValueError("oper must be one of '+', '/', '-', or '*'")

# class that reduces fraction class with integer numerator and denominator
class Fraction(object):
	def __init__(self, numerator, denominator):
		if denominator == 0:
			raise ZeroDivisionError("denominator cannot be zero")
		elif type(numerator) is not int or type(denominator) is not int:
			raise TypeError("numerator and denominator must be integers")
		def gcd(a,b):
			while b != 0:
				a, b = b, a % b
			return a
		common_factor = gcd(numerator, denominator)
		self.numer = numerator // common_factor
		self.denom = denominator // common_factor
	def __str__(self):
		if self.denom != 1:
			return "{} / {}".format(self.numer, self.denom)
		else:
			return str(self.numer)
	def __float__(self):
		return self.numer / self.denom
	def __eq__(self, other):
		if type(other) is Fraction:
			return self.numer == other.numer and self.denom == other.denom
		else:
			return float(self) == other
	def __add__(self, other):
		return Fraction(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)
	def __sub__(self, other):
		return Fraction(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)
	def __mul__(self, other):
		return Fraction(self.numer * other.numer, self.denom * other.denom)
	def __truediv__(self, other):
		if self.denom * other.numer == 0:
			raise ZeroDivisionError("cannot divide by zero")
		return Fraction(self.numer * other.denom, self.denom * other.numer)

# function that determines if the cards a, b, and c constitute a set
from itertools import combinations
def is_set(a, b, c):
	y = 0
	for i in range(4):
		# if the sum of the ith integers is divisible by 3, increment y by 1
		if (int(a[i]) + int(b[i]) + int(c[i])) % 3 == 0:
			y += 1
		else:
			return False
	# if all of the sums of the ith integers are divisible by 3, return true
	if y == 4: 
		return True

# function that returns the number of sets in the provided Set hand
def count_sets(cards): 
	for i in range(len(cards)):
		# if there aren't 12 cards, raise an error
		if len(cards) != 12:
			raise ValueError("there are not exactly 12 cards")
		# if the cards aren't unique (uses a set which only has unique elements), raise an error
		elif len(cards) != len(set(cards)):
			raise ValueError("the cards are not all unique")
		# if the length of each card isn't 4, raise an error
		elif len(cards[i]) != 4:
			raise ValueError("one or more cards does not have exactly 4 digits")
		# if the digits of each card isn't 0, 1, or 2, raise an error
		elif {cards[i][0], cards[i][1], cards[i][2], cards[i][3]}.issubset({"0", "1", "2"}) == False:
		 	raise ValueError("one or more cards has a character other than 0, 1, or 2")
		else: 
			x = 0
			# find all combinations of the Set hand
			for combos in (combinations(cards, 3)):
				# use is_set function to test if the combination is a set
				if is_set(str(combos[0]), str(combos[1]), str(combos[2])):
					# if the combination is a set, increment x by 1
					x += 1
				# if the combination isn't a set, keep x as is
				else:
					x = x
			# return the number of sets
			return x
