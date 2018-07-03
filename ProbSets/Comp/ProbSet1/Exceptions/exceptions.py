# EXCEPTIONS

# Problem 1

def arithmagic():
	step_1 = input("Enter a 3-digit number where the first and last digits differ by 2 or more: ")
	x = True
	# while loop that continues until the user enters a valid number
	while x:
		# checks if the number is 3 digits		
		if len(step_1) != 3:
			raise ValueError("This number is not a 3-digit number")
		# checks if the first and last digit differ by less than 2
		elif abs(int(step_1[0]) - int(step_1[2])) < 2:
			raise ValueError("This number’s first and last digits differ by less than 2")
		else:
			x = False
	x = True
	step_2 = input("Enter the reverse of the first number, obtained by reading it backwards: ")
	# while loop that continues until the user enters a valid reverse number
	while x:
		for i in range(len(step_2)):
			# compares the first digit of the first number with the last digit of the second and works its way in
			if step_1[i] != step_2[len(step_2) - 1 - i]:
				raise ValueError("This is not the reverse of the first number")
		x = False
	x = True
	step_3 = input("Enter the positive difference of these numbers: ")
	# while loop that continues until the user enters a valid difference
	while x:
		# checks the difference of the two numbers
		if int(step_3) != abs(int(step_1) - int(step_2)):
			raise ValueError("This is not the positive difference of the numbers")
		else:
			x = False
	x = True
	step_4 = input("Enter the reverse of the previous result: ")
	# while loop that continues until the user enters a valid reverse number
	while x:
			for i in range(len(step_4)):
				# compares the first digit of this number with the last digit of the third number and works its way in
				if step_3[i] != step_4[len(step_4) - 1 - i]:
					raise ValueError("This is not the reverse of the third number")
			x = False
	print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")

# Problem 2

from random import choice
def random_walk(max_iters = 1e12):
	try: 
	    walk = 0
	    directions = [1, -1]
	    for i in range(int(max_iters)):
	        walk += choice(directions)
	# if the user raises a Keyboardinterrupt, print the following statement
	except KeyboardInterrupt as k:
		print("Process interrupted at iteration %i" %i)
	# if the user doesn't raise a Keyboardinterrupt, print the following statement
	else:
		print("Process completed")
	# always return walk
	finally:
		return walk

# Problem 3 and 4

class ContentFilter:
	def __init__(self, filename):
		self.filename = filename
		x = True
		# while loop that continues until the user opens a valid file
		while x:
			try:
				myfile = open(self.filename, 'r')
				contents = myfile.readlines()
				x = False
			except (FileNotFoundError, TypeError, OSError) as e:
				new_name = input("Please enter a valid name: ")
				self.filename = new_name
		# allows contents of the file to be accessible
		self.contents = ''.join(contents)
		myfile.close()
	# method that writes to a file in either all uppercase or all lowercase
	def uniform(self, writename, mode = 'w', case = "upper"):
		self.mode = mode
		self.case = case
		# if the mode isn't a valid mode, raise an error
		if self.mode not in {'w', 'x', 'a'}:
			raise ValueError("mode must be 'w', 'x', or 'a'")
		else:
			# changes all contents to uppercase
			if self.case == "upper":
				case_content = self.contents.upper()
			# changes all contents to lowercase
			elif case == "lower":
				case_content = self.contents.lower()
			# raises an error if the user enters an invalid case
			else:
				raise ValueError("case must be lower or upper")
			# writes changed contents to file and closes file
			with open(writename, mode) as myfile:
				myfile.write(case_content)
	# method that reverses either words or lines
	def reverse(self, writename, mode = 'w', unit = "line"):
		self.mode = mode
		self.unit = unit
		with open(writename, mode) as myfile:
			# reverses lines
			if self.unit == "line":
				# split the contents by line
				reverse_content = self.contents.split("\n")
				lines = len(reverse_content)
				for i in range(lines):
					# write to the file from the last line to the first line
					myfile.write(reverse_content[lines - 1 - i])
					myfile.write("\n")
			# reverses words while keeping the line order
			elif self.unit == "word": 
				# split the contents by line
				line_content = self.contents.split("\n")
				lines = len(line_content)
				for i in range(lines):
					# split each line by words
					reverse_content = line_content[i].split(" ")
					x = len(reverse_content)
					for j in range(x):
						# write to the file from the last word to the first word of each line
						myfile.write(reverse_content[x - 1 - j])
						myfile.write(" ")
					# write a new line so that the lines are kept in order
					myfile.write("\n")
			# raises an error if the user enters an invalid unit
			else:
				raise ValueError("unit must be 'line' or 'word'")
	# method that changes the rows and columns of words
	def transpose(self, writename, mode = 'w'):
		self.mode = mode
		with open(writename, mode) as myfile:
			# split the contents by line
			lines_content = self.contents.split("\n")
			lines = len(lines_content)
			# find the number of columns
			words = len(lines_content[0].split(" "))
			for i in range(words):
				# write the ith word in each row and then iterate through the columns
				for j in range(lines):
					# split each line by words
					words_content = lines_content[j].split(" ")
					# write the ith word to the file
					myfile.write(words_content[i])
					myfile.write(" ")
				# write a new line
				myfile.write("\n")
	# magic method that prints information
	def __str__(self):
		length = len(self.contents)
		lines = len(self.contents.split("\n"))
		whitespace = 0
		digits = 0
		alpha = 0
		# loop through the characters of the file
		for i in range(length):
			# if the character is a space character, increment whitespace by 1
			if self.contents[i].isspace():
				whitespace += 1
			# if the character is a digit, increment digits by 1
			elif self.contents[i].isdigit():
				digits += 1		
			# if the character is an alphabetic character, increment alpha by 1		
			elif self.contents[i].isalpha():
				alpha += 1
		# return the information
		return "Source file: \t\t " + str(self.filename) + "\n" + "Total characters: \t " + str(length) + "\n" + "Alphabetic characters: \t " + str(alpha) + "\n" + "Numerical characters: \t " + str(digits) + "\n" + "Whitespace characters: \t " + str(whitespace) + "\n" + "Number of lines: \t " + str(lines)