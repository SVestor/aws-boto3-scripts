import boto3

def get_boto3_client(service_name, region="us-east-1", profile=None):
    session = boto3.Session(profile_name=profile) 
    
    if profile:
        session = boto3.Session(profile_name=profile)
    else:
        session = boto3.Session()
    
    return session.client(service_name, region_name=region)

if __name__ == '__main__':
    ec2_client = get_boto3_client("ec2", region="us-east-1", profile="cloud-user")

    response = ec2_client.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}")

    s3 = get_boto3_client("s3")  # Uses default profile and region
    buckets = s3.list_buckets()

    for b in buckets['Buckets']:
        print(b['Name'])

