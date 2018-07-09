# CONDITIONING AND STABILITY

import numpy as np
import scipy.linalg as la
from scipy.linalg import norm, qr, solve_triangular
from sympy import poly_from_expr, product, symbols, integrate, exp, N, subfactorial, factorial
from mpmath import e
import matplotlib.pyplot as plt

# PROBLEM 1
# function that computes the condition number of a matrix
def c1(A):
	sig = la.svdvals(A)
	if sig.min() == 0:
		return np.inf
	else:
		return sig.max() / sig.min()
# TEST
A = np.random.random((5, 5))
c1(A) == np.linalg.cond(A)

# PROBLEM 2
# function that carries out the experiment 100 times
def c2(n):
	roots = np.arange(1, n)
	x, i = symbols("x i")
	w = poly_from_expr(product(x - i, (i, 1, n - 1)))[0]
	coeffs = np.array(w.all_coeffs())
	plt.figure(figsize = (10, 7))
	plt.plot(roots, np.zeros(n - 1), "o", label = "Original")
	for i in range(100):
		r = np.random.normal(loc = 1, scale = 1e-10, size = n)
		coeffs1 = coeffs * r
		roots1 = np.roots(np.poly1d(coeffs1))
		roots = np.sort(roots)
		roots1 = np.sort(roots1)
		plt.scatter(roots1.real, roots1.imag, marker = ".", c = "k", s = 2)
	print(f"The absolute condition number in the infinity norm is {norm(roots1 - roots, np.inf) / norm(r):.2f}")
	print(f"The relative condition number in the infinity norm is {norm(roots, np.inf) / norm(roots1, np.inf):.2f}")
	plt.xlabel("Real")
	plt.ylabel("Imaginary")
	plt.legend(["Original", "Perturbed"], loc = "upper left")
	plt.show()
# TEST
c2(20)
	
# PROBLEM 3
# function that estimates the condition number of the eigenvalue problem
def c3(A):
	r = np.random.normal(0, 1e-10, A.shape)
	i = np.random.normal(0, 1e-10, A.shape)
	H = r + 1j * i
	lamb = la.eigvals(A)
	lamb1 = la.eigvals(A + H)
	absolute = norm(lamb - lamb1) / norm(H)
	relative = norm(A) / norm(lamb) * absolute
	return absolute, relative
# TEST
c3(A)

# PROBLEM 4
# function that computes the relative condition number of the eigenvalue problem
def c4(xmin, xmax, ymin, ymax, res):
	xgrid = np.linspace(xmin, xmax, res)
	ygrid = np.linspace(ymin, ymax, res)
	x, y = np.meshgrid(xgrid, ygrid)
	relative = np.empty((res, res))
	for i, xi in enumerate(xgrid):
		for j, yi in enumerate(ygrid):
			A = np.array([[1, xi], [yi, 1]])
			relative[i, j] = c3(A)[1]
	plt.pcolormesh(x, y, relative, cmap = "gray_r")
	plt.colorbar()
	plt.show()
# TEST
c4(-100, 100, -100, 100, 100)

# PROBLEM 5
# function that solves for the coefficients of the polynomial of degree n that best fits the data in stability_data.npy
def c5(n):
	x, y = np.load("stability_data.npy").T
	A = np.vander(x, n+1)
	xinv = la.inv(A.T @ A) @ A.T @ y
	errorinv = norm(A @ xinv - y)
	print(f"The inverse method has a forward error of {errorinv:.2f}") 
	Q, R = la.qr(A, mode = "economic")
	xqr = solve_triangular(R, Q.T @ y)
	errorqr = norm(A @ xqr - y)
	print(f"The QR method has a forward error of {errorqr:.2f}") 
	plt.figure(figsize = (10, 7))
	plt.plot(x, np.polyval(xinv, x), label = "Inverse")
	plt.plot(x, np.polyval(xqr, x), label = "QR")
	plt.plot(x, y, ".", c = "k")
	plt.legend()
	plt.show()
# TEST
c5(14)

# PROBLEM 6
# function that computes I(n) for the same values of n
def c6():
	x = symbols("x")
	lst = np.arange(5, 50, 5)
	err = np.empty(10)
	for i, n in enumerate(lst):
		integral = N(integrate(x ** n * exp(x - 1), (x, 0, 1)))
		subfact = (-1) ** n * subfactorial(n) + (-1) ** (n + 1) * factorial(n) / e
		err[i] = np.abs(integral - subfact)
	plt.plot(np.log(err))
	plt.show()
# TEST
c6()