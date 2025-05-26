import boto3

def list_all_users():
    client = boto3.client('iam')
    
    paginator = client.get_paginator('list_users')
    response_iterator = paginator.paginate()
    
    for response in response_iterator:
        for user in response['Users']:
            user_name = user['UserName']
            user_id = user['UserId']
            user_create_date = user['CreateDate']
            user_arn = user['Arn']
            user_path = user['Path']
            
            print( f"User Name: {user_name}\nUser ID: {user_id}\nUser Create Date: {user_create_date}\nUser ARN: {user_arn}\nUser Path: {user_path}\n")

if __name__ == '__main__':
    list_all_users()
