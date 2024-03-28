# Python program to read json file

import json

# Open the file
file = open("data.json", "r")

# Read the data from the file
data = json.load(file)

# Close the file
file.close()

# Print the data
print(data)
