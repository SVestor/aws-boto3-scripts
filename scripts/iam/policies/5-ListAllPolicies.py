import boto3

def list_all_policies():
    client = boto3.client('iam')
    
    paginator = client.get_paginator('list_policies')
    response_iterator = paginator.paginate(Scope='Local')
    
    for response in response_iterator:
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            policy_id = policy['PolicyId']
            policy_arn = policy['Arn']
            policy_path = policy['Path']
            
            print(f"Policy Name: {policy_name}\nPolicy ID: {policy_id}\nPolicy ARN: {policy_arn}\nPolicy Path: {policy_path}\n")
    

if __name__ == '__main__':
    list_all_policies()
    
