# PAGERANK

import numpy as np
from scipy import linalg as la
from scipy.sparse import dok_matrix

# PROBLEM 1
# function that creates an adjacency matrix from a file
def p1(file, N):
	A = np.zeros((N, N))
	nodes = []
	with open(file, "r") as myfile:
		for i in myfile:
			try:
				node = list(map(int, i.strip().split()))
				nodes.append(node)
			except:
				pass
	for j in range(N):
		for k in range(N):
			if [j, k] in nodes:
				A[j, k] = 1
	return dok_matrix(A)
# TEST
(p1("matrix.txt", 5)).toarray()

# PROBLEM 2
# function that computes and returns the K matrix given an adjacency matrix
def p2(A, N):
	A[A.sum(axis = 1) == 0, :] = np.ones(N)
	D = A.sum(axis = 1)
	return A.T / D
# TEST
p2((p1("matrix.txt", 5)).toarray(), 5)

# PROBLEM 3
# function that uses the iterative method to find the steady state of the PageRank algorithm
def p3(A, N = None, d = 0.85, tol = 1e-5, max_iter = 200):
	if N is None:
		N = A.shape[0]
	A = A[:N+1, :N+1]
	K = p2(A, N)
	p = np.ones(N)
	p = p / p.sum()
	diff = 1e3
	i = 0
	while diff > tol and i < max_iter:
		p1 = d * K @ p + ((1 - d) / N) * np.ones(N)
		diff = np.linalg.norm(p - p1)
		p = p1
		i += 1
	return p
# TEST
p3(p1("matrix.txt", 5).toarray())

# PROBLEM 4
# function that uses the eigenvalue method to find the steady state of the PageRank algorithm
def p4(A, N = None, d = 0.85, tol = 1e-5, max_iter = 200):
	if N is None:
		N = A.shape[0]
	A = A[:N+1, :N+1]
	K = p2(A, N)
	B = d * K + ((1 - d) / N) * np.ones((N, N))
	eigvals, eigvecs = la.eig(B)
	max_eig = eigvals.argmax()
	return eigvecs[:, max_eig] 
# TEST
p4(p1("matrix.txt", 5).toarray())

# PROBLEM 5
# function that produces a comparative ranking of the teams
def p5():
	wl = []
	with open("ncaa2013.csv", "r") as myfile:
		myfile.readline()
		for line in myfile:
			teams = line.strip().split(",")
			wl.append(teams)
	wl = np.array(wl)
	teams = np.unique(wl.flatten())
	N = len(teams)
	team_id = dict(zip(teams, range(N)))
	wl_id = np.array([[team_id[w], team_id[l]] for w, l in wl[:, ]])
	A = np.zeros((N, N))
	for game in wl_id:
		j, i = game
		A[i, j] = 1
	p = p3(A, d = 0.7)
	rank_id = p.argsort()[-5:][::-1]
	return(list(teams[rank_id]))
