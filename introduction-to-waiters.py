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
print(my_req_instance_object.state['Name'])
while True: # this block of code is a waiter, we included our own logic, until the required stage has reached, but no need of manual logic, this type of logic is there with boto3
    my_req_instance_object = ec2_resource.Instance('i-0935755e734f25042')
    print('the current state of the instance is: ' , my_req_instance_object.state['Name'])
    if my_req_instance_object.state['Name']=='running':
        break
    print('waiting for the instance to start')
    time.sleep(5)
print(my_req_instance_object.state['Name'])
print('started the instance')
