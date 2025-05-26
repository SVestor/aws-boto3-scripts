import boto3

def create_user(user_name):
    client = boto3.client('iam')
    response = client.create_user(UserName=user_name)
    print(response)

if __name__ == '__main__':
    create_user('test-user5')

