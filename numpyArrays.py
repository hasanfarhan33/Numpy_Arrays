import numpy as np

# Creating an array using a list
print("")
my_list = [1,2,3,4]
print(my_list)
arr = np.array(my_list)
print(arr)

# Creating a 3 dimensional array
print("")
my_mat = [[1,2,3], [4,5,6], [5,3,5]]
print(my_mat)
matArray = np.array(my_mat)
print(matArray)

#Creating an array just using numpy
numpyArray = np.arange(0, 11, 2)
print(numpyArray)

# Creating an array of zeros
print("")
zeroArray = np.zeros((4, 4))
print(zeroArray)

# Creating an array of ones
print("")
onesArray = np.ones((5,3))
print(onesArray)

# Creating an equally spaced array between two numbers
print("")
linSpaceArray = np.linspace(0, 50, 100)
print(linSpaceArray)

# Creating an identity matrix
print("")
identityMatrix = np.eye(10)
print(identityMatrix)

# A bunch of random functions
# rand
print("")
randArray = np.random.rand(5)
print(randArray)

# randn
print("")
randnArray = np.random.randn(5)
print(randnArray)

# randint
print("")
randIntArray = np.random.randint(1, 100, 11)
print(randIntArray)

# Bunch of useful functions
print(randArray.shape)
print(randArray.reshape(2, 2))
print(randArray.argmax())
print(randArray.argmin())
# print(randArray.max())
# print(randArray.min())