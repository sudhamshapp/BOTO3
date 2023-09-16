# waiters - the script has to wait until your instance is up and running
import boto3
import sys
import time
from boto3.session import Session
import sys
# authenticating the AWS Management Console
aws_management_console = Session()
# Accessing the IAM service
ec2_resource = aws_management_console.resource("ec2")
ec2_client  = aws_management_console.resource("ec2")
print('starting the instance')
my_req_instance_object = ec2_resource.Instance('i-0935755e734f25042')
my_req_instance_object.start()
print("starts the instance")
# print(my_req_instance_object.state['Name'])
# print(dir(my_req_instance_object))
my_req_instance_object.wait_until_running() #waiter - this should be enough rather than the while loop, Resource waiter waits for 200 seconds(40 checks every five seconds, if instance isn't reached the desired state in 200 seconds, it throws an error), this is using the resource object but not the client 
print("Now the instance is up and running")