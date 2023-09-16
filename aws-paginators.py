# standardization
import boto3
client = boto3.client('ec2')
# response = client.describe_instances()
# print(response)
paginator = client.get_paginator('describe_instances')
response_iterator = paginator.paginate()
# print(response_iterator)
for page in response_iterator:
    print(page)
    