# it gonna pull all instance ids in a one go
import boto3
client = boto3.client('ec2')
response = client.describe_instances()
for reservations in response['Reservations']:
    # print(reservations)
    for instance_stuff in reservations['Instances']:
        achieved_instances = (instance_stuff)['InstanceId']
        print(achieved_instances)

# it gonna pull the single-instance id
# import boto3
# client = boto3.client('ec2')
# response = client.describe_instances()['Reservations'][0]['Instances'][0]['InstanceId']
# print(response)

# when we load json into a python object, it converts into a python dictionary
