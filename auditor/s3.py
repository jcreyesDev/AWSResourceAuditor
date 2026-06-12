import boto3

def get_buckets_info():
    session = boto3.Session(profile_name='jcreyescloud')
    client = session.client('s3')
    response = client.list_buckets()
    buckets = response['Buckets']

    result = []

    for bucket in buckets:
        bucket_name = bucket['Name']
        bucket_location = client.get_bucket_location(Bucket=bucket_name)['LocationConstraint'] or 'us-east-1'

        result.append({'Bucket Name': bucket_name, 'Location': bucket_location})

    return result