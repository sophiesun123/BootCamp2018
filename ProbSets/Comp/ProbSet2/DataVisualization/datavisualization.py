# DATAVISUALIZATION

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, special
import math

# Problem 1
# function that plots data and calculates other data values
def d1(): 
	# load in data
	arr = np.load('anscombe.npy')
	x = np.linspace(0, 20, 50)
	x1, y1, x2, y2, x3, y3, x4, y4 = arr[:,0], arr[:,1], arr[:,2], arr[:,3], arr[:,4], arr[:,5], arr[:,6], arr[:,7]
	# plot functions
	ax1 = plt.subplot(221)
	ax1.plot(x1, y1, 'o', markersize=5, alpha=.5)
	s1, i1, r1, p1, sd1 = stats.linregress(x1, y1)
	y12 = s1 * x + i1
	meanx1, meany1 = np.mean(x1), np.mean(y1)
	varx1, vary1 = np.var(x1), np.var(y1)
	ax1.plot(x, y12)
	ax1.set_title("I")
	ax2 = plt.subplot(222)
	ax2.plot(x2, y2, 'o', markersize=5, alpha=.5)
	s2, i2, r2, p2, sd2 = stats.linregress(x2, y2)
	y22 = s2 * x + i2
	meanx2, meany2 = np.mean(x2), np.mean(y2)
	varx2, vary2 = np.var(x2), np.var(y2)
	ax2.plot(x, y22)
	ax2.set_title("II")
	ax3 = plt.subplot(223)
	ax3.plot(x3, y3, 'o', markersize=5, alpha=.5)
	s3, i3, r3, p3, sd3 = stats.linregress(x3, y3)
	y32 = s3 * x + i3
	meanx3, meany3 = np.mean(x3), np.mean(y3)
	varx3, vary3 = np.var(x3), np.var(y3)
	ax3.plot(x, y32)
	ax3.set_title("III")
	ax4 = plt.subplot(224)
	ax4.plot(x4, y4, 'o', markersize=5, alpha=.5)
	s4, i4, r4, p4, sd4 = stats.linregress(x4, y4)
	y42 = s4 * x + i4
	meanx4, meany4 = np.mean(x4), np.mean(y4)
	varx4, vary4 = np.var(x4), np.var(y4)
	ax4.plot(x, y42)
	ax4.set_title("IV")
	plt.suptitle("Exercise 1")
	plt.show()
	print("In section I, the mean and variance of x, the mean and variance of y, slope, intercept, and correlation coefficient, respectively, are " + 
	str(meanx1) + str(meany1) + str(varx1) + str(vary1) + str(s1) + str(i1) + str(r1))
	print("In section II, the mean and variance of x, the mean and variance of y, slope, intercept, and correlation coefficient, respectively, are " + 
	str(meanx2) + str(meany2) + str(varx2) + str(vary2) + str(s2) + str(i2) + str(r2))
	print("In section III, the mean and variance of x, the mean and variance of y, slope, intercept, and correlation coefficient, respectively, are " + 
	str(meanx3) + str(meany3) + str(varx3) + str(vary3) + str(s3) + str(i3) + str(r3))
	print("In section IV, the mean and variance of x, the mean and variance of y, slope, intercept, and correlation coefficient, respectively, are " + 
	str(meanx4) + str(meany4) + str(varx4) + str(vary4) + str(s4) + str(i4) + str(r4))

# PROBLEM 2
# function that plots bernstein number
def b(n, x, v):
	return special.binom(n,v) * x ** v * (1-x) ** (n-v)
def d2():
	counter = 1
	x = np.linspace(0,1,100)
	# plot the first 10 
	for n in range(0,4):
		for v in range(0,4):
			if (v > n) == False:
				y = b(n, x, v)
				plt.subplot(4,4,counter)
				plt.plot(x,y)
				plt.title(r"$b_{}(n,v,x)$".format(n))
				plt.axis([0,1,0,1])
			counter += 1
	plt.show()

# PROBLEM #3
# functions to show correlations between height, weight, and age
def d3(): 
	arr = np.load('mlb.npy')
	h, w, a = arr[:,0], arr[:,1], arr[:,2]
	# height and weight
	x1 = np.linspace(60,75,100)
	ax1 = plt.subplot(131)
	ax1.set_xlim([65, 85])
	ax1.set_ylim([140, 300])
	plt.scatter(h, w, alpha=.5, edgecolor='none')
	s1, i1, r1, p1, sd1 = stats.linregress(h, w)
	y1 = s1 * x1 + i1
	ax1.plot(x1,y1)
	ax1.set_title("Height and Weight")
	# height and age
	x2 = np.linspace(65,90,100)
	ax2 = plt.subplot(132)
	ax2.set_xlim([65,85])
	ax2.set_ylim([20,50])
	plt.scatter(h, a, alpha=.5, edgecolor='none')
	s2, i2, r2, p2, sd2 = stats.linregress(h, a)
	y2 = s2 * x2 + i2
	ax2.plot(x2,y2)
	ax2.set_title("Height and Age")
	# weight and age
	x3 = np.linspace(140,270,100)
	ax3 = plt.subplot(133)
	ax3.set_xlim([140,270])
	ax3.set_ylim([20,50])
	plt.scatter(w, a, alpha=.5, edgecolor='none')
	s3, i3, r3, p3, sd3 = stats.linregress(w, a)
	y3 = s3 * x3 + i3
	ax3.plot(x3,y3)
	ax3.set_title("Weight and Age")
	plt.show()

# PROBLEM 4
# function that visualizes earthquakes
def d4():
	year, magnitude, longitude, latitude = np.load("earthquakes.npy").T
	# histogram for year and number of earthquakes
	c0=c1=c2=c3=c4=c5=c6=c7=c8=c9=c10=0
	for i in range(len(year)):
		yr = math.floor(year[i] + 0.5)
		if yr == 2000:
			c0 += 1
		elif yr == 2001:
			c1 += 1
		elif yr == 2002: 
			c2 += 1
		elif yr == 2003: 
			c3 += 1
		elif yr == 2004: 
			c4 += 1
		elif yr == 2005: 
			c5 += 1
		elif yr == 2006: 
			c6 += 1
		elif yr == 2007: 
			c7 += 1
		elif yr == 2008: 
			c8 += 1
		elif yr == 2009: 
			c9 += 1
		elif yr == 2010: 
			c10 += 1
	years = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"]
	year_positions = np.arange(len(years))
	year_values = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
	ax1 = plt.subplot(121)
	ax1.barh(year_positions, year_values, align="center")
	ax1.set_yticks(year_positions, years)
	ax1.set_title("# Earthquakes")
	# strong and weak earthquakes
	s=w=0
	for i in range(len(magnitude)):
		if magnitude[i] > 6.0 :
			s += 1
		else:
			w += 1
	strength = ["Strong", "Weak"]
	mag_positions = np.arange(len(strength))
	mag_values = [s, w]
	ax2 = plt.subplot(122)
	ax2.bar(mag_positions, mag_values, align="center")
	ax2.set_xticks(mag_positions, strength)
	ax2.set_title("Earthquake Strengths")
	plt.show()
	# location of earthquakes
	ax1 = plt.subplot(121)
	plt.scatter(longitude, magnitude, alpha=.5, edgecolor='none')
	ax1.set_title("Long and Mag")
	ax2 = plt.subplot(122)
	plt.scatter(latitude, magnitude, alpha=.5, edgecolor='none')
	ax2.set_title("Lat and Mag")
	plt.show()

# PROBLEM 5
# function that visualizes the Rosenbrock function
def d5():
	# create a 2-D domain with np.meshgrid()
	x = np.linspace(0, 1.5, 200)
	X, Y = np.meshgrid(x,x)
	g = (1 - X) ** 2 + 100 * (Y - x ** 2) ** x
	# heat map
	ax1 = plt.subplot(121)
	plt.pcolormesh(X, Y, g, cmap="viridis")
	plt.colorbar()
	# contour map
	ax2 = plt.subplot(122)
	plt.contourf(X, Y, g, 10, cmap="inferno")
	plt.colorbar()
	plt.show()