import boto3

def update_user(old_user_name, new_user_name):
    client = boto3.client('iam')
    response = client.update_user(
        UserName=old_user_name, 
        NewUserName=new_user_name)
    
    print(response)
    
if __name__ == '__main__':
    update_user('test-user', 'updated-test-user')
    