import boto3

def delete_user_from_group(user_name, group_name):
    client = boto3.client('iam')
    response = client.remove_user_from_group(
        UserName=user_name,
        GroupName=group_name
    )
    print(response)

# Delete user from group using resource
# Resource is more pythonic way to interact with AWS (high level abstractions)

def delete_user_from_group_v2(user_name, group_name):
    iam = boto3.resource('iam')
    user = iam.User(user_name)
    response = user.remove_group(GroupName=group_name)
    print(response)

# Another way to delete user from group using resource
#     group = iam.Group(group_name)
#     response = group.remove_user(UserName=user_name)
#     print(response)
    
if __name__ == '__main__':
    # delete_user_from_group('test-user5', 'test-group')
    delete_user_from_group_v2('test-user5', 'test-group')
 