# import boto3
# client = boto3.client('ec2')
# response = client.describe_instances()['Reservations'][0]['Instances'][0]['InstanceId']
# print(response)
# for each_value in response:
#     # print(each_value[1]['InstanceId'])
#     id_instance = each_value
#     print(type(id_instance))
import boto3
client = boto3.client('ec2')
# response = client.describe_instances()['Reservations'][0]['Instances'][0]['InstanceId']
response = client.describe_instances()
# instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']
# print(response)
# Initialize a variable to store the found 'InstanceId'
# found_instance_id = None

# # Iterate through the 'Reservations' list
# for reservation in response['Reservations']:
#     # Iterate through the 'Instances' list within each reservation
#     for instance in reservation['Instances']:
#         # Check if 'InstanceId' exists in the current instance
#         if 'InstanceId' in instance:
#             found_instance_id = instance['InstanceId']
#             break  # Exit the loop once 'InstanceId' is found
#     if found_instance_id:
#         break  # Exit the outer loop if 'InstanceId' is found

# if found_instance_id:
#     print("Found Instance ID:", found_instance_id)
# else:
#     print("Instance ID not found in the data.")
# Given JSON data
# Initialize an empty list to store InstanceId values
# instance_ids = []

# Iterate through the 'Reservations' list and extract 'InstanceId' from each 'Instances' dictionary
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        # instance_ids.append(instance_id)
        print(instance_id)

# Now, 'instance_ids' contains all the InstanceId values
# print(instance_ids)




