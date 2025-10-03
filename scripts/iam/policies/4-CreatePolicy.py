import boto3
import json


def create_policy(policy_name, policy_document_path):
    client = boto3.client('iam')

    with open(policy_document_path, 'r') as f:
        policy = json.load(f)  # Load as Python dict

    response = client.create_policy(
        PolicyName=policy_name,
        PolicyDocument=json.dumps(policy)  # Convert to JSON string
    )
    print(response)


if __name__ == '__main__':
    create_policy('s3_list_bucket_policy', './policies/s3_list_bucket.json')
