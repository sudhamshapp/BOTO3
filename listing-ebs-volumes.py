import boto3
from boto3.session import Session
# this library structures the data in a more readable format
from pprint import pprint
aws_management_console = Session()
ec2_console = aws_management_console.client("ec2")
response = ec2_console.describe_volumes()["Volumes"]
# print(response)
for each_volume in response:
    print(each_volume["VolumeId"])
    print(each_volume["AvailabilityZone"])
    print(each_volume["Size"])
    print(each_volume["VolumeType"])
    print(each_volume["SnapshotId"])
    print(each_volume["Iops"])


