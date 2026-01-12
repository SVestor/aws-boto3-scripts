import boto3

def create_login_profile(user_name, password):
    client = boto3.client('iam')
    response = client.create_login_profile(
        UserName=user_name,
        Password=password,
        PasswordResetRequired=True
    )
    print(response)
    
if __name__ == '__main__':
    create_login_profile('test-user', 'Test123!$!')
