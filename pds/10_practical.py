import numpy as np

a1 = np.array([55, 62, 68, 74, 81, 87])
a2 = np.array([[55, 62, 68], [74, 81, 87]])
zeros = np.zeros((2, 3))
ones = np.ones((2, 2))
r = np.arange(1, 7)

print(a1)
print(a2)
print(zeros)
print(ones)
print(r)

print(a2[0, 1])
print(a2[1, 2])

print(a2[:, 1:])
print(a2[0:2, 0:2])

reshaped = a1.reshape(2, 3)
print(reshaped)

b = a2 + 5
print(b)
v = np.array([1, 2, 3])
print(a2 + v)

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(m1 + m2)
print(m1 * m2)
print(np.dot(m1, m2))
print(np.sum(m1))
print(np.mean(m1))
