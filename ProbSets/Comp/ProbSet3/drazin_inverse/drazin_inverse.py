# DRAZIN INVERSE

import numpy as np
from numpy.linalg import matrix_power
from scipy import linalg as la

# PROBLEM 1
# function that determines whether or not A_D is the Drazin inverse of A
def d1(A, k, A_D):
	return np.allclose(A @ A_D, A_D @ A) & np.allclose(matrix_power(A, k + 1) @ A_D, matrix_power(A, k)) & np.allclose(A_D @ A @ A_D, A_D)
# TEST
A = np.array([[1, 3, 0, 0],
              [0, 1, 3, 0],
              [0, 0, 1, 3],
              [0, 0, 0, 0]])
k = 1
A_D = np.array([[1, -3, 9, 81],
                [0, 1, -3, -18],
                [0, 0, 1, 3],
                [0, 0, 0, 0]])
d1(A, k, A_D)
B = np.array([[1, 1, 3],
              [5, 2, 6],
              [-2, -1, -3]])
k = 3
B_D = np.zeros((3, 3))
d1(B, k, B_D)

# PROBLEM 2
# function that computes the drazin inverse
def d2(A, tol):
	n, n = A.shape
	def greater(x):
		abs(x) > tol
	def lessequal(x):
		abs(x) <= tol
	Q1, S, k1 = la.schur(A, sort = greater)
	Q2, T, k2 = la.schur(A, sort = lessequal)
	U = np.hstack([S[:, :k1], T[:, :(n-k1)]])
	U1 = np.linalg.inv(U)
	V = U1 @ A @ U
	Z = np.zeros((n, n))
	if k != 0:
		M1 = np.linalg.inv(V[:k1, :k1])
		Z[:k1, :k1] = M1
	return U @ Z @ U1

# PROBLEM 3
# function that computes the effective resistance from each node to every other node
def d3(A):
	n, n = A.shape
	diag = np.diag(A.sum(axis = 1))
	L = diag - A
	R = np.zeros((n, n))
	for i in range(n):
		for j in range(n):
			L1 = L.copy()
			L1[j, :] = np.eye(n)[j]
			L1 = d2(L1, 1e-5)
			if i != j:
				R[i, j] = L1[i, i]
	return R

# PROBLEMS 4 AND 5
# class that performs link prediction
class LinkPredictor:
	def __init__(self, file):
		self.file = file
		nodes = []
		with open("social_network.csv", "r") as f:
			for line in f:
				nodes.append(line.strip().split(","))
		nodes = np.array(nodes)
		names = np.unique(nodes)
		N = len(names)
		names_id = dict(zip(names, range(N)))
		nodes_id = np.array([[names_id[i], names_id[j]] for i, j in nodes[:, ]])
		A = np.zeros((N, N))
		for x in nodes_id:
			i, j = x
			A[i, j] = 1
			A[j, i] = 1
		self.A = A
		self.names = names
		self.R = d3(A)
	def predict_link(self, node = None):
		R, A = self.R, self.A
		names = self.names
		R[A == 1] = 0
		if node is None:
			min_resist = np.min(R[R > 0])
			loc = np.argwhere(R == min_resist).flatten()
			return (names[loc[0]], names[loc[1]])
		elif node.isalpha():
			if node not in names:
				raise ValueError("node isn't in names")
			i = np.argwhere(names == node)
			Ri = R[:, i]
			min_resist = np.min(Ri[Ri > 0])
			loc = np.argwhere(Ri == min_resist).flatten()
			return (node, names[loc[0]])
	def add_link(self, node1, node2):
		names = self.names
		if node1 not in names or node2 not in names:
			raise ValueError("node isn't in names")
		i = np.argwhere(names == node1)
		j = np.argwhere(names == node2)
		self.A[i, j] = 1
		self.A[j, i] = 1
		self.R = d3(self.A)
# TEST
data = LinkPredictor('social_network.csv')
# Emily and Oliver are most likely to become friends next
data.predict_link()
# Melanie is predicted to become friends with Carol next
data.predict_link('Melanie')
# Alan is expected to become friends with Sonia
data.predict_link('Alan')
data.add_link('Sonia', 'Alan')
# Alan is then expected to become friends with Piers
data.predict_link('Alan')
data.add_link('Piers', 'Alan')
# Alan is then expected to become friends with Abigail
data.predict_link('Alan')