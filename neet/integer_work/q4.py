# q4.py — Dynamic Programming Languages CA 1 — Question 4 (25%)
# Only NumPy and Matplotlib allowed.
# Run: python q4.py
#
# NOTE: The brief asks for "one figure, two subplots side by side" in (e)(6).
# In some environments you might prefer two separate figures; below I show two figures
# to keep things simple to render everywhere. If you NEED subplots, see the commented
# section at the end.

import numpy as np
import matplotlib.pyplot as plt

# (a)
x = np.arange(1, 13)  # 1..12 inclusive
is_even = (x % 2 == 0)

print("Even values:", x[is_even])
print("Odd values:", x[~is_even])

A = x.reshape(3, 4)
print("A shape:", A.shape)

# (b)
A_masked = A.copy()
A_masked[A_masked < 5] = -1

print("A first row (unchanged):", A[0])
print("A_masked first row:", A_masked[0])

# (c)
B = np.arange(13, 25).reshape(3, 4)
S = np.vstack([A, B])

p = np.array([0,1,2,3,4,5,6])
q = np.array([6,5,4,3,2,1,0])

common = np.intersect1d(p, q)
eq_positions = np.where(p == q)[0]

print("Common items between p and q:", common)
print("Positions where p == q:", eq_positions)

# (d)
M = np.array([[1, 2, 3],
              [4, np.nan, 6],
              [7, 8, 9]], dtype=float)

M_swapped = M[:, [2, 1, 0]]  # swap first and last columns
M_clean = M[~np.isnan(M).any(axis=1)]  # drop rows containing NaN

print("M_swapped:\n", M_swapped)
print("M_clean:\n", M_clean)

# (e)
np.random.seed(42)
R = 5 + 5*np.random.random((3, 200))  # uniform in [5,10]
baseline = np.array([5.0, 7.5, 9.0])

D = R - baseline[:, None]  # broadcasting row-wise

np.set_printoptions(precision=3, suppress=True)
print("First 5 values of row 0 of D:", D[0, :5])

# Two separate figures (keeps rendering simple & clear)
row_means = D.mean(axis=1)

plt.figure()
plt.plot([0,1,2], row_means, marker='o')
plt.title("Row-wise means of D")
plt.xlabel("Row index")
plt.ylabel("Mean value")
plt.grid(True)

plt.figure()
plt.hist(D.ravel(), bins=20)
plt.title("Histogram of all values in D")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)

plt.show()

# --- If your environment requires subplots in one figure, use this instead ---
# fig, axes = plt.subplots(1, 2, figsize=(10, 4))
# axes[0].plot([0,1,2], row_means, marker='o')
# axes[0].set_title("Row-wise means of D")
# axes[0].set_xlabel("Row index")
# axes[0].set_ylabel("Mean value")
# axes[0].grid(True)
# axes[1].hist(D.ravel(), bins=20)
# axes[1].set_title("Histogram of all values in D")
# axes[1].set_xlabel("Value")
# axes[1].set_ylabel("Frequency")
# axes[1].grid(True)
# plt.tight_layout()
# plt.show()
