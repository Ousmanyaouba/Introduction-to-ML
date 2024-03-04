import numpy as np

array2 = np.array(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print("Vector:",array2)
a = array2.reshape(3,5)
print("Two dimjensioal array:",a)

print("Shape: ", a.shape)
print("Dimension: ", a.ndim)
print("data type: ", a.dtype.name)
print("Size: ", a.size)
print("type: ", type(a))

x=np.array([1,2,3])
y=np.array([4,5,6])

print(x+y)
print(x-y)
print(x**2)


a=np.array([1,2,3])
d=a.copy()
print(d)
b=a
c=а
b[0]=5
print(a,b,c)


a=np.array([1,2,3,4,5,6,7])
print(a[0])
print (a[0:4])


reverse_array=a[::-1]
print (reverse_array)


b=np.array([[1,2,3,4,5], [6, 7,8,9, 10]])
print(b)
print(b[1,11])
print(b[:,1])
print(b[1,1:4])
print(b[1,1:4])