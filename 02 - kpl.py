# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
# Explanation video: http://youtu.be/JK5ht5_m6Mk
 
# Calculate Miles Per Gallon
print("This program calculates kilometres per litre.")
 
# Get milometres driven from the user
kilometres_driven = input("Enter kilometres driven:")
# Convert text entered to a
# floating point number
kilometres_driven = float(kilometres_driven)
 
# Get litres used from the user
litres_used = input("Enter litres used:")
# Convert text entered to a
# floating point number
litres_used = float(litres_used)
 
# Calculate and print the answer
kpl = kilometres_driven / litres_used
print("Kilometres per litre:", kpl)
