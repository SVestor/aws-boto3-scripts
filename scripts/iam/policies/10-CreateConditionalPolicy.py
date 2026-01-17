import boto3
import json
from datetime import datetime, timezone


def create_policy(policy_name, policy_document_path, start_time, end_time):
    client = boto3.client('iam')

    with open(policy_document_path, 'r') as f:
        policy = json.load(f)  # Load as Python

    # Ensure the policy has at least one condition
    if 'Condition' not in policy['Statement'][0]:
        policy['Statement'][0]['Condition'] = {}
    
    # Add condition to each statement
    for statement in policy['Statement']:
        statement['Condition'] = {
            'DateGreaterThan': {'aws:CurrentTime': start_time},
            'DateLessThan': {'aws:CurrentTime': end_time}
        }

    response = client.create_policy(
        PolicyName=policy_name,
        PolicyDocument=json.dumps(policy)  # Convert to JSON string
    )
    print(f"Policy {policy_name} created: {response['Policy']['Arn']}")


if __name__ == '__main__':
    current_time = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    start_time = f"{current_time}T18:00:00Z"
    end_time = f"{current_time}T21:00:00Z"
    create_policy('s3_get_object', './policies/s3_get_object.json', start_time, end_time)
