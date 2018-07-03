# OBJECTED ORIENTED

# Problem 1 and 3

# create a Backpack class with 3 arguments
class Backpack:
    def __init__(self, name, color, max_size = 5):
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []
    # method that puts an item into the backpack
    def put(self, item):
    	# if the backpack is already at max_size, don't put the item in
    	if len(self.contents) == self.max_size:
    		print("No Room!")
    	# if the backpack isn't at max_size, put the item in
    	else:
        	self.contents.append(item)
    # method that empties the backpack
    def dump(self):
    	self.contents = []
    # magic method that checks if two backpacks are the same
    def __eq__(self, other):
    	return self.name == other.name and self.color == other.color and len(self.contents) == len(other.contents)
    # magic method that prints information
    def __str__(self):
        return "Owner: \t\t " + str(self.name) + "\n" + "Color: \t\t " + str(self.color) + "\n" + "Size: \t\t " + str(len(self.contents)) + "\n" + "Max Size: \t " + str(self.max_size) + "\n" + "Contents: \t " + str(self.contents)

def test_backpack():
    testpack = Backpack("Barry", "black")
    if testpack.name != "Barry":
        print("Backpack.name assigned incorrectly")
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item)
    print("Contents:", testpack.contents)
    print(str(testpack))

test_backpack()

# Problem 2

# class that inherits from Backpack
class Jetpack(Backpack): 
	def __init__(self, name, color, max_size = 2):
		Backpack.__init__(self, name, color, max_size)
		# set default fuel to 10
		self.fuel = 10	
	# method that decrements fuel by amt_fuel	
	def fly(self, amt_fuel):	
		# if the amount decremented is greater than the amount of fuel left, print the following
		if amt_fuel > self.fuel:
			print("Not enough fuel!")
		# if the amount decremented is less than the amount of fuel left, decrement the fuel
		else:
			self.fuel -= amt_fuel
	# overrides dump method by emptying fuel and contents
	def dump(self):				
		self.fuel = 0
		self.contents = []

# Problem 4

# create a ComplexNumber class with 2 arguments
from math import sqrt
class ComplexNumber:
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag
	# return a ComplexNumber that negates the imaginary part
	def conjugate(self):
		return ComplexNumber(self.real, -self.imag)
	# magic method that returns a string
	def __str__(self):
		# if the real component is 0, just return the imaginary part
		if self.real == 0:
			return "("+ str(self.imag) + "j" + ")"
		# if the real component isn't 0, return the imaginary part with the correct + or - 
		else:
			if self.imag >= 0:
				return "(" + str(self.real) + "+" + str(self.imag) + "j" + ")"
			else:
				return "(" + str(self.real) + "-" + str(abs(self.imag)) + "j" +")"
	# magic method that returns the magnitude
	def __abs__(self):
		return sqrt(self.real ** 2 + self.imag ** 2)
	# magic method that returns whether or not two complex numbers are the same
	def __eq__(self, other):
		return self.real == other.real and self.imag == other.imag
	# magic method that adds two complex numbers
	def __add__(self, other): 
		new_real = self.real + other.real
		new_imag = self.imag + other.imag
		return ComplexNumber(new_real, new_imag)
	# magic method that subtracts two complex numbers
	def __sub__(self, other):
		new_real = self.real - other.real
		new_imag = self.imag - other.imag
		return ComplexNumber(new_real, new_imag)
	# magic method that multiplies two complex numbers
	def __mul__(self, other):
		new_real = self.real * other.real - self.imag * other.imag
		new_imag = self.real * other.imag + self.imag * other.real
		return ComplexNumber(new_real, new_imag)
	# magic method that divides two complex numbers
	def __truediv__(self, other):
		numer = self.__mul__(other.conjugate())
		denom = other.__mul__ (other.conjugate())
		# ensures that the denominator isn't 0 or else it raises an error
		if denom.real == 0:
			raise ZeroDivisionError("denominator is 0")
		else:
			new_real = numer.real / denom.real
			new_imag = numer.imag / denom.real
			return ComplexNumber(new_real, new_imag)

def test_ComplexNumber(a, b, c, d):
	py_cnum, my_cnum = complex(a, b), ComplexNumber(a, b)
	arr_py_cnum, arr_my_cnum = complex(c, d), ComplexNumber(c, d)
	if my_cnum.real != a or my_cnum.imag != b:
		print("__init__() set self.real and self.imag incorrectly")
	if py_cnum.conjugate().imag != my_cnum.conjugate().imag:
		print("conjugate() failed for", py_cnum)
	if str(py_cnum) != str(my_cnum):	
		print("__str__() failed for", py_cnum)
	if abs(py_cnum) != abs(my_cnum):
		print("__abs__() failed for", py_cnum)
	if (py_cnum == arr_py_cnum) != (my_cnum == arr_py_cnum):
		print("__eq__() failed for", py_cnum)
	if py_cnum + arr_py_cnum != my_cnum + arr_py_cnum:
		print("__add__() failed for", py_cnum)
	if py_cnum - arr_py_cnum != my_cnum - arr_py_cnum:
	 	print("__sub__() failed for", py_cnum)
	if py_cnum * arr_py_cnum != my_cnum * arr_py_cnum:
		print("__mul__() failed for", py_cnum)
	if py_cnum / arr_py_cnum != my_cnum / arr_py_cnum:
		print("__truediv__() failed for", py_cnum)


