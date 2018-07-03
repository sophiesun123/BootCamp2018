# EXERCISE 8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

# PART A
# function that makes a 2D hist of cholesterol with 25 bins
def a():
	# only get diseased data
	l = pd.read_csv('lipids.csv', skiprows=4)
	l = l[l.diseased == 1]
	# make hist
	counts, bins, _ = plt.hist(l['chol'], bins=25)
	plt.xlabel('Cholesterol')
	plt.ylabel('Frequency')
	plt.show()
	# find midpoint of bin with highest freq
	print("The midpoint of the bin with the highest frequency is " + str(bins[[counts.argmax(), counts.argmax()+1]].mean()))

# PART B AND C
# function that makes a 3D hist of cholesterol and trigliceride with 25 bins
# much help from Natasha
def b():
	# only get diseased data
	l = pd.read_csv('lipids.csv', skiprows=4)
	l = l[l.diseased == 1]
	# make hist
	fig = plt.figure(figsize=(15, 15))
	ax = fig.add_subplot(111, projection='3d')
	hist, xedges, yedges = np.histogram2d(l['chol'], l['trig'], bins=25)
	xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
	xpos = xpos.flatten('F')
	ypos = ypos.flatten('F')
	zpos = np.zeros_like(xpos)
	dx = xedges[1] - xedges[0]
	dy = yedges[1] - yedges[0]
	dz = hist.flatten()
	cmap = cm.get_cmap('jet')
	max_height = np.max(dz)
	min_height = np.min(dz)
	rgba = [cmap((k - min_height) / max_height) for k in dz] 
	ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=rgba, zsort='average', edgecolor='k')
	plt.xlabel("Cholesterol")
	plt.ylabel("Trigliceride")
	ax.set_zlabel('Frequency')
	plt.show()
	print("Low cholesterol and trigliceride levels are positively correlated. I'd say that this group, people with low cholesterol and trigliceride levels, have the highest risk for heart disease.")