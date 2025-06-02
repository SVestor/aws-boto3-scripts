import boto3

def attach_policy_to_group(group_name, policy_arn):
    client = boto3.client('iam')
    response = client.attach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )
    print(response)
    
if __name__ == '__main__':
    policy_arn = "arn:aws:iam::339712849641:policy/s3_list_bucket"
    attach_policy_to_group('test-group', policy_arn)
      