# Numerical package - numpy (scipy) - Matrix operation important for Data science, array
import numpy as np
# import datetime as dt 

# array and array operation
a = np.array([1, 2, 3, 4])
a + 1

b = np.ones(4) + 1

2**a  # powers of 2
a - b # difference 
j = np.arange(500)
2**(j + 1) - j # power of two and subtract

mm = np.array(([1,2],[3,4]))
2**(mm + 1) - mm # power of two and subtract

# basic matrices
c = np.ones((3, 3))
c * c # element-wise
c.dot(c) # matrix np.dot(c,c)
np.zeros((2,3)) # matrix of zeros
np.eye(4) # unit matrix
np.eye(4,10) # unit matrix
np.zeros((3, 3, 3)) # higher dimension

# compare
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
c = np.array([1, 2, 3, 4])
a == b
a > b
np.array_equal(a, b)
np.array_equal(a, c) # np.all(a == c)
np.all(a == b)
np.all(a == c)
(a == c).all() # all True
(a == b).any() # at least one True
(a == c).any()

a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
np.logical_or(a, b)
np.logical_and(a, b)

# any or all
a = np.zeros((100, 100))
np.any(a != 0)
a[0][0] = 1
np.any(a != 0)
np.any(a == 0)
np.all(a == a)
a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
((a <= b) & (b <= c)).all() # and != &. Check!
((a >= b) & (b <= c)).all()
((a >= b) & (b <= c)).any()

a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 1, 4, 5])
((a <= b) & (b <= c)).all()
((a <= b) | (b <= c)).all()

# works with length of 1
((a <= b) and (b >= c))
((a <= b) or (b <= c))

a = np.array([1])
b = np.array([2])
c = np.array([6])
((a <= b) and (b >= c))
((a <= b) or (b <= c))


# universal functions
a = np.arange(500000)
np.sin(a)
np.log(a)
np.exp(a)

a = np.array([4, 3, 1, 2])
np.max(a) # index of max - y
np.min(a) # index of min - y
np.argmax(a) # index of max - x 
np.argmin(a) # index of min - x


x = np.array([1, 2, 3, 4])
np.sum(x)
x.sum()

x = np.array([[1,2,3], [3,4,8]])
x.sum(axis=0) # columns, run through
x.sum(axis=1) # rows

x = np.random.rand(2, 2, 2)
x = np.array([[[1,2,3], [3,4,8]],[[1,2,3], [3,4,8]]])

x.sum(axis=0)  # first or last block
x.sum(axis=1)  # up or down
x.sum(axis=2)  # left or right

x.sum(axis=2)[0, 1]     
x[0, 1, :].sum() 
x[0,1,:]

# reshape or broadcast
a = np.arange(9).reshape(3, 3)
a = np.arange(36).reshape(4, 9).reshape(2,18)
a.T

# tile and repeat

np.arange(0, 40, 10)

np.tile(np.arange(0, 40, 10), (3))
np.tile(np.arange(0, 40, 10), (1, 3))
a = np.tile(np.arange(0, 40, 10), (3,2))

np.tile(np.arange(0, 40, 10), (3, 1))
a = np.tile(np.arange(0, 40, 10), (3, 1)).T
a
np.tile(np.arange(0, 40, 10), (1, 3))
np.tile(np.arange(0, 40, 10), (3, 1))

b = np.array([0, 1, 2])
a + b

a = np.arange(0, 40, 10)
a.shape
a = a[:, np.newaxis]  # adds a new axis -> 2D array
a.shape
a
a = a[:, np.newaxis, np.newaxis]
a.shape

A = np.arange(12).reshape(3,4)
b = np.repeat(A, 2, axis=0) 
b = np.repeat(A[:,:,np.newaxis], 2, axis=2) 
b = np.repeat(A[:,:,np.newaxis], 2, axis=1)
b = np.repeat(A[np.newaxis,:,:], 2, axis=0)
b = np.repeat(A[:,:,np.newaxis], 2, axis=0)

np.tile(A, (2,1,1))  # add a new dimension at the beginning
np.repeat(A[None,:,:], 2, axis=0) # add a new dimension at the beginning
np.tile(A, (1,1,2))

x, y = np.arange(5), np.arange(5)[:, np.newaxis]
distance = np.sqrt(x ** 2 + y ** 2)
distance = x + y


# ravel and flatten
a = np.array([[1, 2, 3], [4, 5, 6]])
a.flatten()
a.ravel()
a.T # row wise
a.T.ravel() # row wise
a.T.flatten() # row wise

np.array([[1, 2, 3], [4, 5, 6]]).flatten()

x = np.array([[[0], [1], [2]]])
x.shape

# squeeze
x.shape
np.squeeze(x)
np.squeeze(x).shape

# linspace
b = np.linspace(0.0, 10.0, num=101)
np.sin(b)

# sort
a = np.array([4, 3, 1, 2])
a.sort()
a = np.array([4, 3, 1, 2])
j = np.argsort(a)
a[j] # by sorted index
a[np.array([1,0,1,0,1,2])]

# statistic
x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
x.mean()
y.mean(axis=1)
np.median(x)
np.median(y)
np.median(y, axis=-1) # last axis
x.std()     
np.std(y,axis=0)

# generating array using random numbers
rg = np.random.default_rng(1234) # set.seed in R
a = np.floor(10 * rg.random((2, 2)))
b = np.floor(10 * rg.random((2, 2)))

np.vstack((a, b)) # row on row
np.hstack((a, b)) # col to col


# simpler matrix
A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

A = np.array( [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]])

print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
C = A.dot(B)
A.transpose()

# scipy, tensor

# https://scipy-lectures.org/intro/numpy/operations.html
# https://numpy.org/doc/stable/user/quickstart.html
# https://jakevdp.github.io/PythonDataScienceHandbook/02.03-computation-on-arrays-ufuncs.html
# https://towardsdatascience.com/10-numpy-functions-you-should-know-1dc4863764c5
# https://www.oreilly.com/library/view/python-for-data/9781449323592/ch04.html
# https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/VectorizedOperations.html
# https://www.datacamp.com/community/tutorials/python-numpy-tutorial