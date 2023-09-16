import boto3
import sys
from boto3.session import Session
import sys
# authenticating the AWS Management Console
aws_management_console = Session()
# Accessing the IAM service
random_resource = aws_management_console.resource("ec2")
ec2_client  = aws_management_console.client("ec2")
# print(dir(ec2_resource.instances))
'''
for each_stuff in random_resource.instances.all():
    print(each_stuff.id)
'''

'''
all_instances_ids = [] #taking a empty list to append the instances ids using the for loop
for each_stuff in random_resource.instances.all():
    all_instances_ids.append(each_stuff.id)
print(all_instances_ids)    
'''



'''
print('starting all instances')
random_resource.instances.start()
waiter = ec2_client.get_waiter('instance_running') #from documentation, this is the waiter object, fetched the whole stuff from documentation, 40 checks for every 15 seconds
waiter.wait(InstanceIds = all_instances_ids)

print('starting all instances')
'''
'''
desired_server_ids = []
f1 = {"Name": "tag:Name", "Values": ["mars"]}
for each_instance in random_resource.instances.filter(Filters=[f1]):
    desired_server_ids.append(each_instance.id)
print(desired_server_ids)    
'''


desired_server_ids = []
f1 = {"Name": "tag:Name", "Values": ["mars"]}
for each_item in ec2_client.describe_instances(Filters=[f1])['Reservations']:
    for each_instance in each_item['Instances']:
        desired_server_ids.append(each_instance['InstanceId'])
print(desired_server_ids)
print('starting all instances')
ec2_client.start_instances(InstanceIds=desired_server_ids)
waiter = ec2_client.get_waiter('instance_running')
waiter.wait(InstanceIds=desired_server_ids)
print("instance with mars tag are running")