# MATPLOTLIB

import numpy as np
import matplotlib.pyplot as plt

# Problem 1
# function that creates a nxn array of values and computes the mean and variance
def m1(n): 
	arr = np.random.normal(size=(n,n))
	# compute mean of each row
	means = np.mean(arr, axis=1)
	# return var of means
	return (np.var(means))

# function that creates an array of the var of nxn arrays and plots the result
def m(): 
	x = []
	y = []
	for i in range(10):
		val = 100 + (i+1)
		x.append(val)
		y.append(m1(val))
		plt.plot(x, y)
	plt.show()

# Problem 2
# function that plot sin, cos, and arctan
def m2(): 
	# create array of evenly spaced values with 100 points
	x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
	# define functions
	y1 = np.sin(x)
	y2 = np.cos(x)
	y3 = np.arctan(x)
	# plot functions
	plt.plot(x, y1)
	plt.plot(x, y2)
	plt.plot(x, y3)
	plt.show()

# Problem 3
# function that plots the f(x) = 1 / (x - 1) curve
def m3(): 
	# separate domains
	x1 = np.linspace(-2, 1)
	y1 = 1 / (x1 - 1)
	x2 = np.linspace(1, 6)
	y2 = 1 / (x2 - 1)
	# plot separate parts of the function
	plt.plot(x1, y1, 'k--', color = 'm', linewidth=4)
	plt.plot(x2, y2, 'k--', color = 'm', linewidth=4)
	# restrict the domain and range
	plt.xlim(-2,6)
	plt.ylim(-6,6)
	plt.show()

# Problem 4
# function that plots functions in subplots
def m4():
		# create array of evenly spaced values with 100 points
	x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
	# define functions
	y1 = np.sin(x)
	y2 = np.sin(2 * x)
	y3 = 2 * np.sin(x)
	y4 = 2 * np.sin(2 * x)
	# plot functions
	ax1 = plt.subplot(221)
	ax1.plot(x, y1, color = 'g')
	plt.axis([0, 2 * np.pi, -2, 2])
	ax1.set_title("Sin(x) Graph")
	ax2 = plt.subplot(222)
	ax2.plot(x, y2, 'k--', color = 'r')
	plt.axis([0, 2 * np.pi, -2, 2])
	ax2.set_title("Sin(2x) Graph")
	ax3 = plt.subplot(223)
	ax3.plot(x, y3, 'k--', color = 'b')
	plt.axis([0, 2 * np.pi, -2, 2])
	ax3.set_title("2sin(x) Graph")
	ax4 = plt.subplot(224)
	ax4.plot(x, y4, 'k--', color = 'm')
	plt.axis([0, 2 * np.pi, -2, 2])
	ax4.set_title("2sin(2x) Graph")
	plt.suptitle("Exercise 4")
	plt.show()

# Problem 5
# function that visualizes data for FARS
def m5():
	# load in data
	arr = np.load('FARS.npy')
	# define x and y
	hr = arr[:,0]
	lon = arr[:,1]
	lat = arr[:,2]
	# scatterplot
	ax1 = plt.subplot(121)
	ax1.plot(lon, lat, 'k,')
	plt.xlabel("Longitude")
	plt.ylabel("Latitude")
	plt.axis("equal")
	# histogram
	ax2 = plt.subplot(122)
	ax2.hist(hr, bins=24, range = [0,24])
	plt.xlabel("Hour")
	plt.show()

# Problem 6
# function that plots (sin(x) * sin(y)) / (x * y)
def m6():
	# create a 2-D domain with np.meshgrid()
	x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
	y = x.copy()
	X, Y = np.meshgrid(x,y)
	g = (np.sin(X) * np.sin(Y)) / (X * Y)
	# heat map
	ax1 = plt.subplot(121)
	plt.pcolormesh(X, Y, g, cmap="viridis")
	plt.colorbar()
	plt.axis([-2 * np.pi, 2 * np.pi, -2 * np.pi, 2 * np.pi])
	# contour map
	ax2 = plt.subplot(122)
	plt.contour(X, Y, g, 10, cmap="coolwarm")
	plt.colorbar()
	plt.axis([-2 * np.pi, 2 * np.pi, -2 * np.pi, 2 * np.pi])
	plt.show()