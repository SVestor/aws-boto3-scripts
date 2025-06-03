import boto3

def deactivate_access_key(user_name, access_key_id):
    client = boto3.client('iam')
    response = client.update_access_key(
        UserName=user_name,
        AccessKeyId=access_key_id,
        Status='Inactive'
    )
    print(response)
    
if __name__ == '__main__':
    deactivate_access_key('test-user5', 'AKIAZI2LH2O4VNTWDMXZ')
