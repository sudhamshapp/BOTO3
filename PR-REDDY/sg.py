
import boto3
client = boto3.client('ec2')
response = client.describe_security_groups(GroupIds=['sg-0ae68ce8b581fcb79'])['SecurityGroups'][0]['IpPermissions']
# print(type(response))
# print(response)
def checkrules():
    for each_element in response:
        # print(each_element['IpRanges'][0]['CidrIp'])
        if each_element['IpRanges'][0]['CidrIp'] == '0.0.0.0/0': 
            # here each_element is one inbound rule
            client.revoke_security_group_ingress(GroupName = 'sid-sg',IpPermissions = [each_element])
            print('yes')
            # print(each_element)
        else:
            print('Rules are as per standards')
def lambda_handler(event, context):
    checkrules()




'''
import boto3
client = boto3.client('ec2')
response = client.describe_security_groups()['SecurityGroups']
# print(response)
for each_element in response:
    # print(each_element['GroupId'])
    # sg_id = each_element['GroupId']
    for each_elements in each_element:
    # print(each_element['IpRanges'][0]['CidrIp'])
        if each_elements['IpRanges'][0]['CidrIp'] == '0.0.0.0/0': 
            # here each_element is one inbound rule
            # client.revoke_security_group_ingress(GroupName = 'sid-sg',IpPermissions = [each_element])
            print('yes')
            # print(each_element)
        else:
            print('Rules are as per standards')

'''



'''
import boto3
client = boto3.client('ec2')
response = client.describe_security_groups(GroupIds=['sg-0ae68ce8b581fcb79'])['SecurityGroups'][0]['IpPermissions']
# print(type(response))
# print(response)
for each_element in response:
    # print(each_element['IpRanges'][0]['CidrIp'])
    if each_element['IpRanges'][0]['CidrIp'] == '0.0.0.0/0': 
        # here each_element is one inbound rule
        client.revoke_security_group_ingress(GroupName = 'sid-sg',IpPermissions = [each_element])
        print('yes')
        # print(each_element)
    else:
        print('Rules are as per standards')
'''



'''
# this was created using the resource method
import boto3
ec2 = boto3.resource('ec2', region_name="us-west-2") # client is the method, the variable is arbitary here
sg = ec2.SecurityGroup('sg-044e37dc4d39517e7')
rules = sg.ip_permissions
# print(rules)
def checkrules():
    for rule in rules:
        for sourcerange in rule["IpRanges"]:
            if sourcerange["CidrIp"] == "0.0.0.0/0":
                sg.revoke_ingress(IpPermissions=[rule])
                print("Deleted: security gropup id: {} Rule: {}" .format(sg.group_id, rule))
            else:
                print("Rules as per standard")    


def lambda_handler(event, context):
    checkrules()
'''    




    

