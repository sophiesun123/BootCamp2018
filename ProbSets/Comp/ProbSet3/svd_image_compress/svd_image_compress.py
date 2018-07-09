# SVD IMAGE COMPRESS

import numpy as np
from scipy import linalg as la
import matplotlib.pyplot as plt
import scipy.misc

# PROBLEM 1
# function that calculates the compact svd algorithm
def svd1(A):
	lam, V = la.eig(A.conj().T @ A)
	sig = np.sqrt(lam)
	sig = sig[np.argsort(sig)[::-1]]
	V = V[np.argsort(sig)[::-1]]
	r = (sig != 0).sum()
	sig1 = sig[:r]
	V1 = V[:, :r]
	U1 = A @ V1 / sig1
	return U1, sig1, V1.conj().T
# TEST
A = np.random.random((10,5))
U,s,Vh = la.svd(A, full_matrices=False)
U1, s1, Vh1 = svd1(A)
print(U.shape, s.shape, Vh.shape)
np.allclose(U1.T @ U1, np.identity(5))
np.allclose(U1 @ np.diag(s1) @ Vh1, A)
np.linalg.matrix_rank(A) == len(s1)

# PROBLEM 2
# function that visualizes the svd
def svd2(A):
	angle = np.linspace(0, 2 * np.pi, 100)
	S = np.vstack([np.cos(angle), np.sin(angle)])
	E = np.array([[1, 0, 0], [0, 0, 1]])
	U, sig, V = la.svd(A)
	diag = np.diag(sig)
	# plot
	fig, axes = plt.subplots(2, 2, figsize = (10, 8))
	def graph(x):
		return x, V @ x, diag @ V @ x, U @ diag @ V @ x
	labels = ['$S$', '$V^HS$', '$\Sigma V^H S$', '$U \Sigma V^H S$']
	for ax, p1, p2, l in zip(axes.flatten(), graph(S), graph(E), labels):
		ax.plot(p1[0], p1[1])
		ax.plot(p2[0], p2[1])
		ax.set_title(l, fontsize=16)
		ax.axis('equal')
	plt.tight_layout()
	plt.show()
# TEST
A = np.array([[3, 1], [1, 3]])
svd2(A)

# PROBLEM 3
# function that computes the compact svd and then truncates it
def svd3(A, s):
	m, n = A.shape
	if s > np.linalg.matrix_rank(A):
		raise ValueError('s is greater than number of nonzero singular values of A')
	else:
		i = m * s + s + n * s
		U, sig, V = la.svd(A)
		U1 = U[:, :s]
		sig1 = sig[:s]
		V1 = V[:s, :]
	return U1 @ np.diag(sig1) @ V1, i
# TEST
A = np.random.random((6, 6))
svd3(A, 2)

# PROBLEM 4
# function that computes the compact svd and lowest rank approximation
def svd4(A, eps):
	U, sig, V = la.svd(A)
	if eps < sig.min():
		raise ValueError("epsilon value is too small")
	else:
		s = len(sig[sig > eps])
		U1 = U[:, :s]
		sig1 = sig[:s]
		V1 = V[:s, :]
		return U1 @ np.diag(sig1) @ V1
# TEST
A = np.random.random((6, 6))
svd4(A, 0.2)

# PROBLEM 5
# function that computes the best rank-s approximation of an image
def svd5(file, s):
	im = plt.imread(file) / 255
	if im.ndim == 3:
		C = []
		v_total = 0
		for i in range(3):
			color = im[:, :, i]
			color_s, v = svd3(color, s)
			v_total += v
			color_s[color_s < 0] = 0
			color_s[color_s > 1] = 1
			C.append(color_s)
		return np.dstack(C), v_total
	elif im.ndim == 2:
		im_s, v = svd3(im, s)
		im_s[im_s < 0] = 0
		im_s[im_s > 1] = 1
		return im_s, v
# TEST
compressed_image, v_compressed = svd5('hubble.jpg', 20)
image = plt.imread('hubble.jpg') / 255
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image)
axes[1].imshow(compressed_image)
plt.suptitle(f'Difference in number of entries = {image.size - v_compressed}')
plt.show()