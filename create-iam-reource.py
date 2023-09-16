# create a iam user
import boto3
client = boto3.client('iam')
# response = client.describe_instances()
# print(response)
response = client.create_user(UserName='Bob')
print(response)
