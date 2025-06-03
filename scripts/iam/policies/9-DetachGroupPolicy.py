import boto3

def detach_policy_from_group(group_name, policy_arn):
    client = boto3.client('iam')
    response = client.detach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )
    print(response)
    
if __name__ == '__main__':
    policy_arn = "arn:aws:iam::637423571897:policy/s3_list_bucket"
    detach_policy_from_group('test-group', policy_arn)
      