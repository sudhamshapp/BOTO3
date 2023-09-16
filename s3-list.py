import boto3
from boto3.session import Session
# authenticating the AWS Management Console
aws_management_console = Session()
# Accessing the S3 service
s3_console = aws_management_console.resource("s3")
for each_bucket in s3_console.buckets.all():
    print(each_bucket.name)
    print(each_bucket.creation_date)

