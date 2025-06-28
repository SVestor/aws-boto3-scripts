import boto3

def create_instance_profile(role_name):
    client = boto3.client('iam')
    response = client.create_instance_profile(
        InstanceProfileName=role_name
    )
    print(f"Response: {response['ResponseMetadata']['HTTPStatusCode']}\nInstance profile {role_name} with ID {response['InstanceProfile']['InstanceProfileId']} created")

def add_role_to_instance_profile(role_name, instance_profile_name):
    client = boto3.client('iam')
    response = client.add_role_to_instance_profile(
        InstanceProfileName=instance_profile_name,
        RoleName=role_name
    )
    print(f"Response: {response['ResponseMetadata']['HTTPStatusCode']}\nRole {role_name} added to instance profile {instance_profile_name}")
    
if __name__ == '__main__':
    create_instance_profile('test-ec2-role')
    add_role_to_instance_profile('test-ec2-role', 'test-ec2-role')
