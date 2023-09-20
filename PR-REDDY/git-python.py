# How can I get the volume id from the event below?import boto3
'''
import boto3
client = boto3.client('ec2')
response = client.modify_volume(VolumeId = volume_id, VolumeType = 'gp3')
event = {
  'version': '0',
  'id': '51abdb0f-0d4d-9836-527c-328a9068fd27',
  'detail-type': 'EBS Volume Notification',
  'source': 'aws.ec2',
  'account': '907360093445',
  'time': '2023-09-20T06:18:14Z',
  'region': 'us-west-2',
  'resources': [
    'arn:aws:ec2:us-west-2:907360093445:volume/vol-027de140f947ca88d'
  ],
  'detail': {
    'result': 'available',
    'cause': '',
    'event': 'createVolume',
    'request-id': '9614eae4-a143-4bcd-81db-d41bfd450e4d'
  }
}
'''



# volume_id = event['resources'][0].split('/')[-1]

# sudhamsh = 'arn:aws:ec2:us-west-2:907360093445:volume/vol-027de140f947ca88d'
# converts the string into a list and removes the '/' if it presents b/w the string
# mars = sudhamsh.split('/')  
# print(mars)
# volume_id = sudhamsh.split('/')[-1]
# print(volume_id)



import boto3

def lambda_handler(event, context):
    # Extract the volume_id from the event
    volume_id = event['resources'][0].split('/')[-1]
    
    # Create an EC2 client
    client = boto3.client('ec2')
    
    # Modify the volume type
    response = client.modify_volume(VolumeId=volume_id, VolumeType='gp3')
    
    # You can add additional logic here as needed
    
    # Return a response if required
    # return {
    #     'statusCode': 200,
    #     'body': 'Volume type modified successfully.'
    # }
