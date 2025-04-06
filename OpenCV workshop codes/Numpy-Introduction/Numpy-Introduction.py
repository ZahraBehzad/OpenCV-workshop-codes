from numpy import *
a = arange(15).reshape(3,5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))

b = array([6, 7, 8])
print(b)
print(type(b))

a = array([2, 3 ,4])
print(a)
print(a.dtype)

b = array([1.2, 3.5, 5.1])
print(b.dtype)

b = array([(1.5, 2, 3),
           (4, 5, 6)])
print(b)

c = array([[1, 2], [3, 4]], dtype= complex)
print(c)

print(zeros((3, 4)))
print(ones((2, 3, 4), dtype= int16))
print(empty((2, 3)))

print(arange(10, 30, 5))
print(arange(0, 2, 0.3))

print(linspace(0, 2, 9))
x = linspace(0, 2*pi, 100)
print(x)
print(sin(x))

print(arange(6))
print(arange(12).reshape(4, 3))
print(arange(24).reshape(2, 3, 4))

a = array([20, 30, 40, 50])
b = arange(4)
print(b)
print(a - b)
print(b**2)
print(10 * sin(a))
print(a < 35)

A = array([[1, 1], [0, 1]])
B = array([[2, 0], [3, 4]])
print(A * B)
print(dot(A, B))

a = ones((2, 3), dtype=float)
b = random.random((2, 3))
a *= 3
print(a)
b += a
print(b)
a += b
print(a)
print(b)

B = arange(3)
print(B)
print(exp(B))
print(sqrt(B))
C = array([2., -1., 4.])
print(C)
print(add(B, C))

a = random.random((2, 3))
print(a)
print(a.sum())
print(a.min())
print(a.max())

b = arange(12).reshape(3, 4)
print(b)
print(b.sum(axis= 0))
print(b.min(axis= 1))
print(b.cumsum(axis= 1))

#Indexing, Slicing, Iterating & Reshaping
a = arange(10)**3
print(a)
print(a[2])
print(a[2:5])
print(a[:6:2])
print(a[::-1])

def f(x, y):
    return 10 * x + y
b = fromfunction(f, (5, 4), dtype=int)
print(b)
print(b[2, 3])
print(b[0:5, 1])
print(b[:, 1])
print(b[1:3, :])

c = array([[[0, 1, 2],
            [10, 12, 13]],
            
            [[100, 101, 102],
             [110, 112, 113]]])
print(c.shape)
print(c[1, ...])
print(c[..., 2])

for row in b:
    print(row)

for element in b.flat:
    print(element)

a = floor(10 * random.random((3, 4)))
print(a)
print(a.shape)
print(a.ravel())
a.shape = (6, 2)
print(a.transpose())
print(a)
a.resize((2, 6))
print(a)
print(a.reshape(3, -1))

#Stacking & Splitting arrays
a = floor(10 * random.random((2, 2)))
print(a)
b = floor(10 * random.random((2, 2)))
print(b)
print(vstack((a, b)))
print(hstack((a, b)))

a = floor(10 * random.random((2, 12)))
print(a)
print(hsplit(a, 3))

#Copy & views
c = a.view()
print(c is a)
print(c.base is a)
print(c.flags.owndata)
c[0, 4] = 1234
print(a)

s = a[ : , 1:3]
s[:] = 10
print(a)

d = a.copy()
print(d is a)
print(d.base is a)
d[0, 0] = 9999
print(a)

#Numpy methods
a = array([[1.0, 2.0], [3.0, 4.0]])
print(a)
print(a.transpose())

u = eye(2)
print(u)

j = array([[0.0, -1.0], [1.0, 0.0]])
print(dot(j, j))

a = array([[3, 1], [1, 2]])
b = array([9, 8])
x = linalg.solve(a, b)
print(x)

