# Problem 5

import box as b
import time
import random
import sys
# checks that user input 3 things
if len(sys.argv) == 3:
	# save user's name as name
	name = sys.argv[1]
	# save user's desired time as t
	t = float(sys.argv[2])
	# initialize the user's list with numbers 0-9
	lst = list(range(1,10))
	# start the clock
	start = time.time()
	# while loop that continues for as long as there's time left
	while round(t - (time.time() - start)) > 0. : 
		# if the user has shut the box (list is empty), exit the loop
		if lst == []:
			break
		# if the user hasn't shut the box (list isn't empty)
		else:
			# if the sum of the list is greater than 6, roll two die
			if sum(lst) > 6:
				roll = random.randint(2,12)
			# if the sum of the list is less than 6, roll one dice
			else: 
				roll = random.randint(1,6)
		# use box.py to check if there are possible combinations of the user's list that sum up to the roll
		if b.isvalid(roll,lst):
			print("Numbers left: " + str(lst)) 
			print("Roll: %i" % roll)
			x = True
			# while loop that promps the user for valid numbers to eliminate
			while x:
				print("Seconds left: %f seconds " % round(t - (time.time() - start)))
				el = input("Numbers to eliminate: ")
				# use box.py to check if the user's input is in the list
				ints_to_el = b.parse_input(el, lst)
				# if the user's input isn't in the list, continue through the while loop
				if ints_to_el == []:
					print("Invalid input")
				# if the user's input is in the list, check if the sum is equal to the roll
				else:
					# if the sum is equal to the roll, remove the numbers from the list and exit the loop
					if sum(ints_to_el) == roll:
						for i in range(len(ints_to_el)):
						  lst.remove(ints_to_el[i])
						x = False
		# if the user can't shut the box, exit the loop
		else:
			break
	# game won message
	if lst == []: 
		print("Score for player %s: %f points" % (name, sum(lst)))
		print("Time played: %f seconds" % round(t - (time.time() - start)))
		print("Congratulations!! You shut the box!")
	# game lost message
	else:
		print("Score for player %s: %f points" % (name, sum(lst)))
		print("Time played: %f seconds" % round(t - (time.time() - start)))
		print("Better luck next time >:)")
# if the user didn't provide 3 arguments, print the following
else:
	print("Please provide the file name, player's name, and a time limit.")








