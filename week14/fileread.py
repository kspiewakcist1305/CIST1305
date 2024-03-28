# Read data from file and print it out

# Open the file
file = open("data.dat", "r")

# Read the data from the file
data = file.read()

# Close the file
file.close()

# Print the data
print(data)
