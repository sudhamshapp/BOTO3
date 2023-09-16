'''
import boto3
client = boto3.client('s3')
response = client.list_objects(Bucket='sudhamsh-tf')['Contents']
# print(response)
count = 1
for each_object in response:
    print(count, each_object['Key'])
    count += 1
'''
import boto3
client = boto3.client('s3')
# response = client.list_objects(Bucket='sudhamsh-tf')
paginator = client.get_paginator('list_objects')
response_iterator = paginator.paginate(Bucket='sudhamsh-tf')
count = 1
for each_object in response_iterator:
    # print("page")
    for each_object_key in each_object['Contents']:
        print(count, each_object_key['Key'])
        count += 1
