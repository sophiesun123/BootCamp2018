# LEAST SQUARES AND EIGENVALUES

import numpy as np
from scipy import linalg as la
import matplotlib.pyplot as plt
import cmath

# PROBLEM 1
# function that accepts a matrix and vector and solves Ax = b
def ls1(A, b):
	Q, R = la.qr(A, mode="economic") 
	return la.solve_triangular(R, Q.T @ b)

# PROBLEM 2
# function that solves for housing price index and year and plots result
def ls2():
	# load in data
	data = np.load('housing.npy')
	# find year and price indices 	
	yr = data[:,0]
	p = data[:,1]
	# construct matrix A and vector b
	A = np.column_stack((yr, np.ones((len(yr)))))
	b = np.vstack(p)
	# find least squares solution
	sol = ls1(A, b)
	# plot data 
	plt.scatter(yr, p)
	plt.xlabel("Year")
	plt.ylabel("Housing Price Index")
	plt.title("Housing Price Index and Year")
	# plot least squares line
	x = np.linspace(0,17,100)
	y = float(sol[0]) * x + float(sol[1])
	plt.plot(x,y)
	plt.show()

# PROBLEM 3
# function that calculates polynomials to fit housing.npy data
def ls3():
	# load in data
	data = np.load('housing.npy')
	# find year and price indices 	
	yr = data[:,0]
	p = data[:,1]
	x_coord = np.linspace(0,17,100)
	# construct matrix A and vector b for degree 3, 6, 9, 12
	for i in range(4, 14, 3):
		# get vanders for each degree
		A = np.vander(yr, i)
		b = np.vstack(p)
		# find coefficients
		x = la.lstsq(A, b)[0]
		# flatten array to use poly1d function
		x = np.ndarray.flatten(x)
		# write the function
		f = np.poly1d(x)
		# use the function to find all y values using the equation and x_coords
		y = np.ndarray.flatten(f(x_coord))
		# plot data
		plt.plot(x_coord, y)
		plt.scatter(yr, p)
		plt.xlabel("Year")
		plt.ylabel("Housing Price Index")
		plt.title("Housing Price Index and Year")
		plt.show()

# PROBLEM 4
# function that finds the best ellipse fit for ellipse.npy data
def plot_ellipse(a, b, c, d, e):
	theta = np.linspace(0, 2*np.pi, 200)
	cos_t, sin_t = np.cos(theta), np.sin(theta)
	A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
	B = b*cos_t + d*sin_t
	r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)
	plt.plot(r*cos_t, r*sin_t, lw=2)
	plt.gca().set_aspect("equal", "datalim")
def ls4():
	 # load data
	data = np.load("ellipse.npy")
	x = data[:, 0]
	y = data[:, 1]
	A = np.array([x ** 2, x, x * y, y, y ** 2]).T
	b = np.ones(len(A))
	sol = ls1(A, b)
	plot_ellipse(*sol)
	plt.scatter(x, y)
	plt.show()

# PROBLEM 5
# function that calculates the power method algorithm
# max iterations
N = 100
tol = 1e-8
def ls5(A): 
	m, n = A.shape
	x = np.random.random(n)
	x = x / la.norm(x)
	k = 0
	diff = 1e3
	while (k < N) & (diff > tol):
		x_kp1 = A @ x
		x_kp1 = x_kp1 / la.norm(x_kp1)
		diff = la.norm(x_kp1 - x)
		x = x_kp1
		k = k + 1
	return (x.T @ A @ x), x

# PROBLEM 6
# function that calculates the QR algorithm
N = 100
tol = 1e-8
def ls6(A):
	m, n = A.shape
	S = la.hessenberg(A)
	for k in range(N):
		Q, R = la.qr(S, mode="economic") 
		S = R @ Q
	eigs = []
	i = 0
	while i < n:
		m1, n1 = (S[i]).shape
		if (S[i, i] == np.diag(S)[-1]):
			eigs.append(S[i, i])
		elif (S[i + 1, i] < tol):
			eigs.append(S[i, i])
		else:
			a, b, c, d = S[i: i + 2, i: i + 2].flatten()
			x = (a + d) + (cmath.sqrt((a + d)**2 - 4 * (a * d - b * c))) / 2
			y = (a + d) - (cmath.sqrt((a + d)**2 - 4 * (a * d - b * c))) / 2
			eigs.extend([x, y])
			i += 1
		i +=1 
	return eigs