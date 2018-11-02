# Part B
# A calculator to find the area of a trapezoid

# Print a title exlaining what the calculator does
print("The area of a trapezoid")


# Ask the user for the necessary inputs
trap_height = input("Enter the height of the trapezoid:")
trap_bottom = input("Enter the length of the bottom base:")
trap_top = input("Enter the length of the top base:")

# Convert all the inputs into 'float' values
trap_height = float(trap_height)
trap_bottom = float(trap_bottom)
trap_top = float(trap_top)

# Use the values to calculate the area
area = 0.5 * (trap_top + trap_bottom) * trap_height

# Print the result to the screen
print("The area is:", area)



