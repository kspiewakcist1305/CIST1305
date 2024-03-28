# Replace specific line in file

# Open the file
file = open("data.dat", "r")

# Read the data from the file
data = file.readlines()

# Close the file
file.close()

# Loop over lines and find the line to replace
for i in range(len(data)):
    print(data[i].lower())
    if "do not panic!" in data[i].lower():
        # Replace the line
        data[i] = "Ok, maybe panic a little...\n"
        break

# Open the file
file = open("data.dat", "w")

# Write data to the file
file.writelines(data)

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
