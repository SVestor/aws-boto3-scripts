import boto3


def list_user_tags(user_name):
    client = boto3.client('iam')
    response = client.list_user_tags(UserName=user_name)
    tags = response['Tags'] # list of tags
    for tag in tags:
        print(f"{tag['Key']}: {tag['Value']}")
    
if __name__ == '__main__':
    list_user_tags('test-user5')
