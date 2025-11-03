import boto3

def delete_login_profile(user_name):
    client = boto3.client('iam')
    response = client.delete_login_profile(UserName=user_name)
    print(response)
    
if __name__ == '__main__':
    delete_login_profile('test-user')
      