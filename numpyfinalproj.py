import numpy as np

# arrays are one of numpy's most useful features
array_a = np.zeros(5) # this creates an array filled with five zeros.
print("Array with five elements, all zero:\n", array_a)
print("The type of this array:\n", type(array_a[0])) 
# we can access elements of the array by typing its name and
# index, we can see that each element of this array is of type float

# we can also create an array with a starting value, ending value, and
# the number of elements we want to create
array_a1 = np.arange(0, 10, 2)
print('this creates an array with values 0, 2, 4, 6, 8: ', array_a1)


                         
# here, we can use shape to see the rows x cols of an array
array_b = [[1, 2, 3, 4], [5, 6, 7, 8]]
print("Normal printing of the array:\n", array_b)
array_b_flipped = np.flip(array_b)
print("Array reversed:\n", array_b_flipped)

array_b = np.array(array_b)
print("Second array neatly printed by row and column:\n", array_b)
# using shape to see the number of rows and columns in the array
print("The number of rows and columns in the array:\n", array_b.shape)

# we can use reshape to change the number of rows and columns (must still equate to same
# number of elements)
array_b1 = array_b.reshape(4,2)
print("Reshaped array:\n", array_b1)
print("The number of rows and columns in the reshaped array:\n", array_b1.shape)

# We can use numpy's library to create an array of random ints
np.random.seed(1) # we have to set the seed so that it generates the same random numbers
array_c = np.random.randint(10, size = 5) # range of possible ints, and the size of the array
print("Array with filled with five random integers from 0 - 10:\n", array_c)

# Various mathematical operations that can be used with numpy
array_d = np.random.randint(100, size = 10) # create an array of 20 ints between 0-100
print("Array filled with 10 random integers, from 0 - 100:\n", array_d)
print("Sum:\n", np.sum(array_d)) 
print("Product:\n", np.prod(array_d))
print("Mean:\n", np.mean(array_d))
print("Standard Deviation:\n", np.std(array_d))
print("Variance:\n", np.var(array_d))
print("Smallest Number:\n", np.min(array_d))
print("Biggest Number:\n", np.max(array_d))
print("All the numbers square rooted:\n", np.sqrt(array_d))
print("All the numbers squared:\n", np.square(array_d))

# to do exponenets in numpy, we use the power function, where 3 can take the place of the exponent
print("All the numbers squared cubed:\n", np.power(array_d, 3))

# we can also use the absolute value function to find the absolute value of an array
print("Absolute value of the array:\n", np.abs(array_d))

# we can also use the sort functin to sort the array
print("Sorted array:\n", np.sort(array_d))

# we can also use the transpose function to transpose the array
array_l = np.array([[1, 2, 3], [4, 5, 6]])
print("Array filled with 10 random integers, from 0 - 100:\n", array_l)
print("Transposed array:\n", np.transpose(array_l))



# We can use comparisons to see where elements are greater or less than a certain value
array_e = np.array([3, 5, 9, 18, 2, 4])
print("Elements in the array that are less than 5:\n", array_e < 5)
print("Elements in the array that are greater than 5:\n", array_e > 5)
# You can also check what the actual values are in the array that are less than a certain number
print("Values in the array less than 6:\n", array_e[array_e < 6])

# This array has 3 dimensions, 4 rows, 5 columns
array_ex = np.random.randint(10, size = (3, 4, 5))
print("3D array:\n", array_ex)

# You can use numpy's unique to find the unique values in an array list
array_f = np.array([1, 3, 5, 7, 9, 1, 3, 4, 9])
print("Array example:\n", array_f)
unique_f = np.unique(array_f)
print("The unique values in the example array:\n", unique_f)


# we can also use various mathematical operations between arrays
array_g = np.array([1, 2, 3, 4, 5])
array_h = np.array([6, 7, 8, 9, 10])
print("Array g:\n", array_g)
print("Array h:\n", array_h)
print("Array g + array h:\n", array_g + array_h)
print("Array g - array h:\n", array_g - array_h)
print("Array g * array h:\n", array_g * array_h)
print("Array g / array h:\n", array_g / array_h)
print("Array g % array h:\n", array_g % array_h)
print("Array g ** array h:\n", array_g ** array_h)

# we can also use the dot function to multiply two arrays
print("Dot product of the two arrays:\n", np.dot(array_g, array_h))


print("We can even add a certain number to each index within the array. For example lets add 30 to each index:\n")
array_i = np.array([1, 2, 3, 4, 5])
array_j = np.array([6, 7, 8, 9, 10])
print("Array i:\n", array_i)
print("Array i + 30:\n", array_i + 30)
print("Array_i @ array_j:\n", array_i @ array_j)


