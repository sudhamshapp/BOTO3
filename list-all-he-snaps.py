import boto3
import sys
from boto3.session import Session
import sys
# authenticating the AWS Management Console
aws_management_console = Session()
# Accessing the IAM service
ec2_client  = aws_management_console.client("ec2")
# filter_for_snapshots = {'Name': 'encrypted', 'Values': ['false']}
# response = ec2_client.describe_snapshots(Filters=[filter_for_snapshots])
# filter_based_on_account_id = {'Name': 'owner-id', 'Values': ['907360093445']} # we can also fetch sts account using sts
# filter_based_on_snapshot_size  = {'Name': 'volume-size', 'Values': ['1']}
# combined_filter = [{'Name': 'owner-id', 'Values': ['907360093445']}, {'Name': 'volume-size', 'Values': ['1']}]
# response = ec2_client.describe_snapshots(Filters=[filter_based_on_account_id], [filter_based_on_snapshot_size])["Snapshots"]
# response = ec2_client.describe_snapshots(Filters=[combined_filter])

print(response)
# for each_snap in response:
#     print(each_snap)
#     print(each_snap["Description"])
#     print(each_snap["VolumeId"])
#     print(each_snap["StartTime"])
#     print(each_snap["State"])
