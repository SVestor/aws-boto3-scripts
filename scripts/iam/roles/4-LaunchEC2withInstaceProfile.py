import boto3

def launch_ec2_with_instance_profile(image_id, instance_type, key_name, security_group_id, instance_profile_name):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId=image_id,
        MinCount=1, # minimum number of instances to launch. Must be 1 or more.
        MaxCount=1, # maximum number of instances to launch. Must be 1 or more.
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group_id],
        IamInstanceProfile={
            'Name': instance_profile_name
        }
    )
    instance_id = instance[0].id
    print(f"Instance: {instance_id} launched with a custom instance profile: {instance_profile_name}")
    
if __name__ == '__main__':
    launch_ec2_with_instance_profile(
        'ami-05ffe3c48a9991133',
        't2.micro',
        'test-key-pair',
        'sg-04b7943e8c7c36d87',
        'test-ec2-role'
    )
