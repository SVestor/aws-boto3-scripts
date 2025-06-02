import boto3

def create_user_group(group_name):
    client = boto3.client('iam')
    response = client.create_group(GroupName=group_name)
    print(response)
    
if __name__ == '__main__':
    create_user_group('test-group')
    