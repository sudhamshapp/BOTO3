# on instances collection object
import boto3
import sys
from boto3.session import Session
import sys
# authenticating the AWS Management Console
aws_management_console = Session()
# Accessing the IAM service
ec2_resource = aws_management_console.resource("ec2")
ec2_client  = aws_management_console.client("ec2")
# print(dir(ec2_resource.instances))
# print(ec2_resource.instances.all())
# response = (ec2_resource.instances.all())
f1 = {'Name': 'instance-state-name','Values': ['running', 'stopped']}
f2 = {'Name': 'instance-state-name','Values': ['t2.micro']}
response = (ec2_resource.instances.filter(Filters=[f1, f2]))
for each_item in response:
    print(each_item)



