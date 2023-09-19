# data = open('error.log', 'r')
# print(data.read()) # Here data is a object and read is the method to read the data from the object.
# data.close()

# with open('error.log', 'r') as data: # Here we are using with statement to open the file and close it automatically.
#     file = (data.read())
# print(type(file))


# import yaml
# with open('data.yml', 'r') as data: 
#     file = yaml.safe_load(data)
# print(type(file))
# print(file)

import json
with open('practice.json', 'r') as data: 
    file = json.load(data)
print(type(file))
print(file['email'])