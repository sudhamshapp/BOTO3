# Retrieves the aws account id
import boto3
from boto3.session import Session
aws_management_console = Session()
sts_console = aws_management_console.client("sts")
response = sts_console.get_caller_identity()
print(response.get('Account')) # retrieving the aws account id

