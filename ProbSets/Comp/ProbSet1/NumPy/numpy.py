# NUMPY

import numpy as np

# define matrices a and b according to the pset
a = np.array([[3, -1, 4], [1, 5, -9]])
b = np.array([[2, 6, -5, 3], [5, -8, 9, 7], [9, -3, -2, -3]])

# function that multiplies two matrices
def np1(a, b):
   return a @ b

# calculate the matrix multiplication
np1(a, b)

# define matrix c according to the pset
c = np.array([[3, 1, 4], [1, 5, 9], [-5, 3, 1]])

# function that calculates the equation
def np2(c):
	return -(np1(c, c) @ c) + 9 * np1(c, c) - 15 * c
	# return - c @ c @ c + 9 * c @ c - 15 * c

# calculate the equation
np2(c)

# define matrices d and e according to the pset
d = np.ones((7, 7), dtype = np.int)
el = np.tril(d * -1)
eu = np.triu(d * 5, 1)
e = el + eu

# function that calculates ABA 
def np3(d, e):
	return (np.triu(d) @ e @ np.triu(d)).astype(np.int64)

# calculate the equation
np3(d, e)

# function that eliminates elements less than 0
def np4(f):
	g = np.copy(f)
	mask = g < 0
	g[mask] = 0
	print(g)

# define matrices h, i, and j according to the pset
h = (np.arange(6).reshape((3,2))).T
i = np.tril(3 + np.zeros((3, 3), dtype = np.int))
j = np.diag([-2, -2, -2])
identity = np.eye(3).astype(np.int64)

# function that creates and returns the block matrix
def np5(h, i, j, identity):
	r1 = np.hstack((np.zeros((3, 3), dtype = np.int), h.T, identity))
	r2 = np.hstack((h, np.zeros((2, 2), dtype = np.int), np.zeros((2, 3), dtype = np.int)))
	r3 = np.hstack((i, np.zeros((3, 2), dtype = np.int), j))
	return np.vstack((r1, r2, r3))

# create the final block matrix
np5(h, i, j, identity)

# function that returns the new-stochastic matrix
def np6(k):
	# find sum of each row
	sum = k.sum(axis = 1).reshape(-1, 1)
	return k / sum

# ffunction that returns the greatest product
grid = np.load("grid.npy")
def np7(grid):
	hmax = np.max(grid[:,:-3] * grid[:,1:-2] * grid[:,2:-1] * grid[:,3:])
	vmax = np.max(grid[:-3, :] * grid[1:-2, :] * grid[2:-1,:] * grid[3:, :])
	drmax = np.max(grid[:-3, :-3] * grid[1:-2, 1:-2] * grid[2:-1, 2:-1] * grid[3:, 3:])
	dlmax = np.max(grid[:-3, 3:] * grid[1:-2, 2:-1] * grid[2:-1, 1:-2] * grid[3:, :-3])
	return max(hmax, vmax, drmax, dlmax)

# return the greatest product
np7(grid)