# waiters - the script has to wait until your instance is up and running
import boto3
from boto3.session import Session
# authenticating the AWS Management Console
aws_management_console = Session()
# Accessing the IAM service
# ec2_resource = aws_management_console.resource("ec2")
ec2_client  = aws_management_console.client("ec2")
print('starting the instance')
ec2_client.start_instances(InstanceIds=['i-0935755e734f25042'])
waiter = ec2_client.get_waiter('instance_running') #from documentation, this is the waiter object, fetched the whole stuff from documentation, 40 checks for every 15 seconds
waiter.wait(InstanceIds=['i-0935755e734f25042'])
print("instance is up and running")
