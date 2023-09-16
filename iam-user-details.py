# retrieving a iam user
import boto3
import datetime
client = boto3.client('iam')
response = client.list_users()['Users']
# print(response)
for each_user in response:
    print(each_user['UserName'])
    print(each_user['Arn'])
    print(each_user['CreateDate'])
    print(each_user['Path'])
    print(each_user['UserId'])
    print(each_user['CreateDate'].strftime("%Y-%m-%d %H:%M:%S"))
