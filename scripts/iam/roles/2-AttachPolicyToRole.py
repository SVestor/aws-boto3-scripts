import boto3

def attach_policy_to_role(role_name, policy_arn):
    client = boto3.client('iam')
    response = client.attach_role_policy(
        RoleName=role_name,
        PolicyArn=policy_arn
    )
    print(f"Response: {response['ResponseMetadata']['HTTPStatusCode']}\nPolicy {policy_arn} attached to role {role_name}")
    
if __name__ == '__main__':
    attach_policy_to_role('test-ec2-role', 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess')
