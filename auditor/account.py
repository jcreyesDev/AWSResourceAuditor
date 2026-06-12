import boto3

def get_account_info():
    session = boto3.Session(profile_name='jcreyescloud')
    client = session.client('sts')
    response = client.get_caller_identity()

    return {'Account': response['Account'], 'UserId': response['UserId'], 'Arn': response['Arn']}