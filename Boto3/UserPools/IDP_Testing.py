import boto3
from dotenv_config import Config
config = Config('.env')

aws_region = Config('aws_region')
aws_access_key_id = Config('aws_access_key_id')
aws_secret_access_key = Config('aws_secret_access_key')

pool = boto3.client(
	service_name='cognito-idp',
	region_name=aws_region,
	aws_access_key_id=aws_access_key_id,
	aws_secret_access_key=aws_secret_access_key
)

Username = "test@example.com"
Email = "test@example.com"
PhoneNumber = "+61400000000"
UserPoolID = 'ap-southeast-2_fakeUserPool'

PoolCreateUser_response = pool.admin_create_user(
	UserPoolId=UserPoolID,
	Username=Username,
	UserAttributes=[
		{
			'Name': 'email',
			'Value': Email
		},
		{
			'Name': 'phone_number',
			'Value': PhoneNumber
		},
	],
	MessageAction='SUPPRESS', # Supresses any email / SMS notification
)
print(PoolCreateUser_response)

#Getting Admin
PoolGetUser_response = pool.admin_get_user(
	UserPoolId=UserPoolID,
	Username=Username,
)
print(PoolGetUser_response)

PoolDeleteUser_response = pool.admin_delete_user(
	UserPoolId=UserPoolID,
    Username=Username
)
print(PoolDeleteUser_response)
