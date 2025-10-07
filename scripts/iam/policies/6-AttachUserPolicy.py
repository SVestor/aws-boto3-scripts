import boto3

def attach_policy_to_user(user_name, policy_arn):
    client = boto3.client('iam')
    response = client.attach_user_policy(
        UserName=user_name,
        PolicyArn=policy_arn
    )
    print(response)
    

if __name__ == '__main__':
    policy_arn = "arn:aws:iam::637423571897:policy/s3_list_bucket"
    attach_policy_to_user('test-user', policy_arn)
