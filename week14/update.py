import json
import os
# function to add to JSON


def write_json(data, filename='data.json'):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump({}, file)

    with open(filename, "r+") as file:
        file_data = json.load(file)
        file_data.update(data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

# python object to be appended
y = {
    "fname": "Sam",
    "lname": "Cooke",
    "phone": "404-123-0005",
    "email": "scooke@noemai.com"
}


write_json(y)
