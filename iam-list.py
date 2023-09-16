import boto3
from boto3.session import Session
# authenticating the AWS Management Console
aws_management_console = Session()
# Accessing the IAM service
iam_console = aws_management_console.resource("iam")
for each_user in iam_console.users.all():
    print(each_user.name)
    print(each_user.arn)
    print(each_user.create_date)