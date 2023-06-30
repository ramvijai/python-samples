# Connect to AWS Parameter store
import boto3

# Get parameter value
ssm = boto3.client('ssm')

def get_parameter(parameter_name):
    response = ssm.get_parameter(Name=parameter_name, WithDecryption=True)
    return response['Parameter']['Value']

def main():
    parameter_name = '/dev/myapp/key1'
    parameter_value = get_parameter(parameter_name)
    print(parameter_value)  

if __name__ == '__main__':  
    main()