# A tuple looks just like a list, except you use parentheses instead of square
# brackets. Once you define a tuple, you can access individual elements by
# using each item’s index, just as you would for a list.


dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# This code tries to change the value of the first dimension, but Python
# returns a type error. Because we’re trying to alter a tuple, which can’t be
# done to that type of object, Python tells us we can’t assign a new value to
# an item in a tuple:

# dimensions[0] = 250
# print(dimensions[0])

for dimension in dimensions:
 print(dimension)

# Although you can’t modify a tuple, you can assign a new value to a variable
# that represents a tuple. For example, if we wanted to change the dimensions
# of this rectangle, we could redefine the entire tuple:


 dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)