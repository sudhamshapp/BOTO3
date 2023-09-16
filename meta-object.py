# used to enter into client  object from resource object
# list available regions for ec2 instance
import boto3
import sys
from boto3.session import Session
import sys
# authenticating the AWS Management Console
aws_management_console = Session()
# Accessing the IAM service
ec2_resource = aws_management_console.resource("ec2")
ec2_client  = aws_management_console.client("ec2")
# print(dir(ec2_resource.meta.client.describe_regions()))
# print(ec2_resource.meta.client.describe_regions()["Regions"])
response = (ec2_resource.meta.client.describe_regions()["Regions"])
for each_region in response:
    print(each_region["RegionName"]) #spits the regions in aws account
