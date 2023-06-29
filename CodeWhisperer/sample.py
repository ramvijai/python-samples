import boto3

def read_file(file_name, bucket):
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, file_name)
    body = obj.get()['Body'].read().decode('utf-8')

    return body


read_file('e36f6ca0-33e7-447c-b593-d633d191d7c9.json', 'cerebro-mes-poc')
