import boto3

def delete_user(user_name):
    client = boto3.client('iam')
    response = client.delete_user(UserName=user_name)
    print(response)
    
if __name__ == '__main__':
    delete_user('test-user')
      