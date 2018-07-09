# QR DECOMPOSITION

import numpy as np
from scipy import linalg as la

# PROBLEM 1
# function that takes a matrix and computes the QR decomposition
def qr1(A):
	# store shape of matrix
	m, n = A.shape
	# make copy
	Q = np.copy(A)
	# matrix of zeroes with dimensions nxn
	R = np.zeros((n,n))
	# for loop
	for i in range(n):
		R[i, i] = la.norm(Q[:, i])
		Q[:, i] = Q[:, i] / R[i, i]
		for j in range(i+1, n): 
			R[i, j] = Q[:, j].T @ Q[:, i]
			Q[:, j] = Q[:, j] - R[i, j] * Q[:, i]
	return Q, R
# TEST
# Generate a random matrix and get its reduced QR decomposition via SciPy.
A = np.random.random((6,6))
# Use mode="economic" for reduced QR
Q, R = la.qr(A, mode="economic") 
Q1, R1 = qr1(A)
print(Q, Q1, R, R1)
# Verify that R1 is upper triangular, Q1 is orthonormal, and QR = A
np.allclose(np.triu(R1), R1)
np.allclose(Q1.T @ Q1, np.identity(6))
np.allclose(Q1 @ R1, A)

# PROBLEM 2
# function that takes an invertible matrix to calculate its determinant
def qr2(A): 
	Q, R = qr1(A)
	return np.prod(np.diag(R))
# TEST
A = np.random.random((6,6))
det = round(abs(la.det(A)))
det1 = round((qr2(A)))
det == det1

# PROBLEM 3
# function that takes an invertible matrix and a vector and solves Ax = b
def qr3(A, b):
	Q, R = qr1(A)
	y = Q.T @ b
	n = y.shape[0]
	x = np.empty((1,n))
	for i in range(n, -1):
		x[0,i] = y[0,i]
		for j in range(i+1, n):
			x[i] = x[i] - R[i, j] * x[j]
		x[i] = x[i] / R[i, i]
	return x

# PROBLEM 4
# function that takes a matrix and completes the householder algorithm
def qr4(A):
	m, n = A.shape
	R = np.copy(A)
	Q = np.identity(m)
	for k in range(n):
		u = np.copy(R[k:, k])
		sign = lambda x: 1 if x >= 0 else -1
		u[0] = u[0] + sign(u[0]) * la.norm(u)
		u = u / la.norm(u)
		R[k:, k:] = R[k:, k:] - 2 * np.outer(u, u.T @ R[k:, k:])
		Q[k:, :] = Q[k:, :] - 2 * np.outer(u, u.T @ Q[k:, :])
	return Q.T, R
# TEST
A = np.random.random((5, 3))
# Get the full QR decomposition
Q,R = la.qr(A)      
Q1, R1 = qr4(A)
print(Q, Q1, R, R1)
np.allclose(Q1 @ R1, A)

# PROBLEM 5
# function that takes a matrix and completes the hessenberg algorithm
def qr5(A):
	m, n = A.shape
	H = np.copy(A)
	Q = np.identity(m)
	for k in range(n-2):
		u = np.copy(H[(k+1):, k])
		sign = lambda x: 1 if x >= 0 else -1
		u[0] = u[0] + sign(u[0]) * la.norm(u)
		u = u / la.norm(u)
		H[(k+1):, k:] = H[(k+1):, k:] - 2 * np.outer(u, u.T @ H[(k+1):, k:])
		H[:, (k+1):] = H[:, (k+1):] - 2 * np.outer(H[:, (k+1):] @ u, u.T)
		Q[(k+1):, :] = Q[(k+1):, :] - 2 * np.outer(u, u.T @ Q[(k+1):, :])
	return H, Q.T
# TEST
# Generate a random matrix and get its upper Hessenberg form via SciPy
A = np.random.random((8,8))
H, Q = la.hessenberg(A, calc_q=True)
H1, Q1 = qr5(A)
# Verify that H has all zeros below the first subdiagonal and Q1HQ1^T = A
np.allclose(np.triu(H1, -1), H1)
np.allclose(Q1 @ H1 @ Q1.T, A)