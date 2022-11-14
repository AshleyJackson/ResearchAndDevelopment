## DynamoDB API
This Terraform Example is used to create a table in DynamoDB and insert data into it.

The ```queryString``` parameter is used to pass the query string to the API and then onto the DynamoDB Database. If the Query string exists in the DB, return the Query String and a True.

If the Query string does not exist in the DB, insert the Query String into the DB and return the Query String and a False.

This example uses the following AWS Services:
* API Gateway
* Lambda
* DynamoDB

### Prerequisites
* Terraform
* AWS Account
