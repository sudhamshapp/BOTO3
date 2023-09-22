'''
import boto3
client = boto3.client('ec2')
# response = client.describe_instances()['Reservations'][0]['Instances'][0]['InstanceId']
response = client.describe_instances()
# Initialize an empty list to store InstanceId values
# instance_ids = []

# Iterate through the 'Reservations' list and extract 'InstanceId' from each 'Instances' dictionary
for reservation in response['Reservations']:
    print(reservation)
    for instance in reservation['Instances']:
        # print(instance)
        instance_id = instance['InstanceId']
        # instance_ids.append(instance_id)
        # print(instance_id)

# Now, 'instance_ids' contains all the InstanceId values
# print(instance_ids)
'''

import boto3
client = boto3.client('ec2')
response = client.describe_instances()
# print(response)
instance_id = []
for reservation in response['Reservations']:
    # print(reservation)
    for instance_detail in reservation['Instances']:
        # print(instance_detail)
        print(type(instance_detail))
        instance_finale = instance_detail['InstanceId']
        # print(instance_finale)
        print(type(instance_finale))
        instance_id.append(instance_finale)
print(instance_id)        



