import boto3

def delete_user_from_group(user_name, group_name):
    client = boto3.client('iam')
    response = client.remove_user_from_group(
        UserName=user_name,
        GroupName=group_name
    )
    print(response)
    
if __name__ == '__main__':
    delete_user_from_group('test-user5', 'test-group')
      