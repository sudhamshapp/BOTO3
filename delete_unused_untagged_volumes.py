# deletion of unused and untagged ebs volumes
import boto3
import sys
from boto3.session import Session
import sys
# authenticating the AWS Management Console
aws_management_console = Session()
# Accessing the IAM service
ec2_client  = aws_management_console.client("ec2")
# using the resource object to fetch the information of all the volumes
'''
ec2_resource = aws_management_console.resource("ec2")
# response = ec2_resource.volumes.all() # all fetches the information of all the volumes, if we want the desired we can use filters instead of all
filter_available_volumes = {'Name': 'status', 'Values': ['available']}
response = ec2_resource.volumes.filter(Filters = [filter_available_volumes])

for each_volume in response:
    if each_volume.tags:
        print(each_volume.id, each_volume.tags)
        print('deleting un-used and un-tagged volmes')
        # each_volume.delete()
    # print(each_volume.state)
print("deleting all the un-tagged volumes")
'''

# fetching the stuff using the client object
response = ec2_client.describe_volumes()['Volumes']
# print(response)
for each_volume in response:
    if not "Tags" in each_volume:        
        print(each_volume['VolumeId'])