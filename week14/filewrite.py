# Append data to file

# Open the file
file = open("data.dat", "a")

# Write data to the file
file.write("\nOk, maybe panic a little...\n")

# Close the file
file.close()

# Open the file
file = open("data.dat", "r")

# Read the data from the file
data = file.read()

# Close the file
file.close()

# Print the data
print(data)
