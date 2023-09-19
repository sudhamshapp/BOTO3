import boto3

client = boto3.client('ec2')
response = client.describe_instances()['Reservations']
# print(response)
for instance_id in response:
    instance_id_retrieval = (instance_id['Instances'][0]['InstanceId'])
    # print(instance_id['Instances'][0]['InstanceId']) - gives the instance-id
    # print(instance_id['Instances'][0]['Tags']) - gives the tags of the instance, the inside stuff in the print, we can iterate using for loop and also apply the condition using if statement
    tag_key_stuff = []
    for tag_key in instance_id['Instances'][0]['Tags']:
        # print(tag_key['Key'])
        tag_key_stuff.append(tag_key['Key']) 
    # print(tag_key_stuff)    
    if 'Application' not in tag_key_stuff:
        print("stop the ec2-intsnce")
        stop_response = client.stop_instances(InstanceIds=[instance_id_retrieval])
    else:
        print("Application tag is presentfor the ec2 instance {}" .format(instance_id_retrieval))
     