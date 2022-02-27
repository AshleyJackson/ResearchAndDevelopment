import boto3
from dotenv_config import Config

config = Config('.env')

# Configurations for App
aws_region = config('aws_region')
aws_access_key_id = config('aws_access_key_id')
aws_secret_access_key = config('aws_secret_access_key')
UserPoolId = config('UserPoolId')
ClientID = '1234567890abcdefghijk'
Username = "test@example.com"
Password = 'password'

# Define connection to Boto3
pool = boto3.client(
	service_name='cognito-idp',
	region_name=aws_region,
	aws_access_key_id=aws_access_key_id,
	aws_secret_access_key=aws_secret_access_key
)

try:
    # Attempt to create the user in the User Pool and then set a password
    pool.admin_create_user(
        UserPoolId=UserPoolId,
        Username=Username,
        TemporaryPassword=Password,
    MessageAction='SUPPRESS',
    )
    pool.admin_set_user_password(
        UserPoolId=UserPoolId,
        Username=Username,
        Password=Password,
        Permanent=True
    )
except:
    # If user already exists, then Delete for this test case.
    pool.admin_delete_user(
        UserPoolId=UserPoolId,
        Username=Username
    )

# Authenticate to User pool as the user and retrieve user specific details e.g. Access Tokens
res = pool.admin_initiate_auth(
    UserPoolId=UserPoolId,
    ClientId=ClientID,
    AuthFlow='ADMIN_NO_SRP_AUTH',
    AuthParameters={
        'USERNAME': Username,
        'PASSWORD': Password
    }
)

print(res)

# Theoretically you could have a third party system that logs in using a third party IDP (Google).
# Once you've logged in with Google, technically you have a "verified" email. From there you could
# use the above code to create a User in a Cognito User Pool and log in with that user.
# Once logged in as the user you can retrieve their Access/Secret Tokens.
# You can then use the secret key ('IdToken') to connect to an API Gateway, if you have the Authorizer's configured
# correctly.