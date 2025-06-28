import boto3
import json

def create_role(role_name, assume_policy_document_path):
    client = boto3.client('iam')
    with open(assume_policy_document_path, 'r') as f:
        assume_policy = json.load(f)
    response = client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(assume_policy)
    )
    print(f"Role {role_name} created: {response['Role']['Arn']}")

if __name__ == '__main__':
    create_role('test-ec2-role', './policies/trust_policy.json')
