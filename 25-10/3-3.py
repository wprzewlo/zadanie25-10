# A program for swapping two variable values
#
x = 7
y = 34
z = 0  # additional, auxiliary variable

print("Before swapping: x =", x, "y =", y)

# Swap the values using the auxiliary variable z
z = x  # Store the value of x in z
x = y  # Assign the value of y to x
y = z  # Assign the value of z (original value of x) to y

print("After swapping: x =", x, "y =", y)

