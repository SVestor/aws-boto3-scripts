import boto3

def delete_access_key(user_name, access_key_id):
    client = boto3.client('iam')
    response = client.delete_access_key(
        UserName=user_name,
        AccessKeyId=access_key_id
    )
    print(response)
    
if __name__ == '__main__':
    delete_access_key('test-user', 'AKIAZI2LH2O4VNTWDMXZ')
      
