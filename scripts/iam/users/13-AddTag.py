import boto3


def add_tag_to_user(user_name, tag_key, tag_value):
    client = boto3.client('iam')
    response = client.tag_user(
        UserName=user_name,
        Tags=[
            {
                'Key': tag_key,
                'Value': tag_value
            }
        ]
    )
    print(f"Tag {tag_key} with value {tag_value} added to user {user_name}")
    

if __name__ == '__main__':
    add_tag_to_user('test-user', 'Department', 'IT')
    add_tag_to_user('test-user', 'Project', 'Test')
    add_tag_to_user('test-user', 'Environment', 'Production')
    add_tag_to_user('test-user', 'CostCenter', 'IT')
    
