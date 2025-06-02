import boto3

def add_user_to_group(user_name, group_name):
    client = boto3.client('iam')
    response = client.add_user_to_group(
        UserName=user_name,
        GroupName=group_name
    )
    print(response)
    
if __name__ == '__main__':
    add_user_to_group('test-user5', 'test-group')
      