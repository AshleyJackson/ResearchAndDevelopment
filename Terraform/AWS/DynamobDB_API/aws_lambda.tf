data "archive_file" "dynamodb" {
  type = "zip"

  source_dir  = "${path.module}/src/"
  output_path = "${path.module}/dist/dynamodb.zip"
}

resource "aws_s3_object" "dynamodb" {
  bucket = "YourBucketHere"

  key    = "dynamodb.zip"
  source = "${path.module}/dist/dynamodb.zip"

  etag = filemd5(data.archive_file.dynamodb.output_path)
}

resource "aws_lambda_function" "dynamodb_api" {
  function_name = "DynamoDB_API"
  timeout       = 30
  runtime       = "nodejs16.x"

  s3_bucket = aws_s3_bucket.dynamodb.id
  s3_key    = aws_s3_object.dynamodb.key

  handler = "index.handler"

  role = aws_iam_role.lambda_exec.arn

}

resource "aws_iam_role" "lambda_exec" {
  name = "serverless_lambda"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Sid    = ""
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role = aws_iam_role.lambda_exec.name

  policy_arn = "arn:aws:iam::aws:policy/AWSLambdaExecute"
}
