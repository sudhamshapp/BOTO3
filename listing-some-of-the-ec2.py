import boto3
from boto3.session import Session
# this library structures the data in a more readable format
from pprint import pprint
aws_management_console = Session()
ec2_console = aws_management_console.client("ec2")
response = ec2_console.describe_instances()["Reservations"]
# print(response) - gives the data in a dictionary format, this contains the actual stuff
# print(type(response)) - gives the data in a dictionary format
# print(response[0]) - gives the data in a dictionary format
# print(response[0]["Instances"]) - gives the data in a dictionary format
for each_item in response: # iterating on top of response
    for each_instance_info in each_item["Instances"]: # iterating on top of each_item        
        # print(each_instance_info["InstanceId"])
        # print(each_instance_info["InstanceType"])
        # print(each_instance_info["LaunchTime"])
        # print(each_instance_info["PrivateIpAddress"])
        # print(f"The Instance Id is: {each_instance_info['InstanceId']}")
        # print(f"The Instance type is: {each_instance_info['InstanceType']}")
        print(f"The Instance Id is: {each_instance_info['InstanceId']}\n", f"The Instance type is: {each_instance_info['InstanceType']}")
        print(f"The launchtime is: {each_instance_info['LaunchTime'].strftime('%Y-%m-%d %H:%M:%S')}") # discloses when the instance was launched

