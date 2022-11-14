const AWS = require('aws-sdk')
AWS.config.update({
	region: 'ap-southeast-2'
}
);

const dynamodb = new AWS.DynamoDB.DocumentClient();
const dynamodbTableName = 'DynamoDBTable';

exports.handler = async (event) => {
	var queryString = event.queryStringParameters?.queryString;
	if (queryString) {
		const response = {
			statusCode: 200,
			body: JSON.stringify({
				queryString: queryString,
				state: await getQueryString(queryString)
			})
		}
		return response
	} else {
		const response = {
			statusCode: 400,
			body: JSON.stringify({
				message: 'Missing Query String'
			})
		}
		return response
	}
}

async function getQueryString(queryString) {
	const params = {
		TableName: dynamodbTableName,
		Key: {
			"id": queryString
		}
	}
	const data = await dynamodb.get(params).promise();
	if (data.Item) {
		return true;
	} else {
		await dynamodb.put({
			TableName: dynamodbTableName,
			Item: {
				"id": queryString
			}
		}).promise();
		return false;
	}
}
