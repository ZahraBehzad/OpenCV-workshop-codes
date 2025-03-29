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