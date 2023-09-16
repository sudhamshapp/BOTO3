# client has too many advantages over resource.
# it's performed only using the resource object, not with the client object.
import boto3
import sys
from boto3.session import Session
import sys
# authenticating the AWS Management Console
aws_management_console = Session()
# Accessing the IAM service
ec2_resource = aws_management_console.resource("ec2")
ec2_client  = aws_management_console.client("ec2")
while True:
    print("This script performs the following actions ec2 instance:  ")
    print(
        "1. Start an EC2 instance\n"
        "2. Stop an EC2 instance\n"
        "3. Terminate an EC2 instance\n"
        "4. exit outta the code\n"
    )
    opt=int(input("Enter your option: "))
    if opt==1:
        instance_id=input("Enter the instance id: ")
        my_req_instance_object = ec2_resource.Instance(instance_id) # we can also hardcode the instace-idif we want, but here the value is getting from the user
        # print(dir(my_req_instance_object)) - spits the list of methods available on the object like stop, start, restart
        my_req_instance_object.start()
        print("starts the ec2-instance")
    elif opt==2:
        instance_id=input("Enter the instance id: ")
        my_req_instance_object = ec2_resource.Instance(instance_id)
        my_req_instance_object.stop()
        print("stops the ec2-instance")
    elif opt==3:
        instance_id=input("Enter the instance id: ")
        my_req_instance_object = ec2_resource.Instance(instance_id)
        my_req_instance_object.terminate()

        print("terminates the ec2-instance")
    elif opt==4:
        sys.exit()
    else:
        print("invalid option")
