import boto3

def remove_tag_from_user(user_name, tag_key):
    client = boto3.client('iam')
    tags = client.list_user_tags(UserName=user_name)['Tags']
    for tag in tags:
        if tag['Key'] == tag_key:
            value = tag['Value']
            response = client.untag_user(
                UserName=user_name,
                TagKeys=[tag_key]
            )
            print(f"Tag {tag_key} with value {value} was successfully removed from user {user_name}")
    
if __name__ == '__main__':
    remove_tag_from_user('test-user', 'Department')
    remove_tag_from_user('test-user', 'Project')
    remove_tag_from_user('test-user', 'Environment')
    remove_tag_from_user('test-user', 'CostCenter')
    
