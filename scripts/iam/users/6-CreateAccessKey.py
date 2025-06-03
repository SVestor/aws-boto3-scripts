import boto3

def create_access_key(user_name):
    client = boto3.client('iam')
    response = client.create_access_key(UserName=user_name)
    print(response)
    
if __name__ == '__main__':
    create_access_key('test-user5')
      