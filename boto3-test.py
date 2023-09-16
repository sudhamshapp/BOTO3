import boto3

client = boto3.client('ec2')
# response = client.describe_instances()
response = client.describe_volumes()
print(response)


