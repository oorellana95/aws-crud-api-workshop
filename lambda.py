# import the JSON utility package
import json
# import the Python math library
import math

# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('aws-crud-api-workshop-dynamodb')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):
    base, exponent = int(event['base']), int(event['exponent'])
    result = math.pow(base, exponent)

# write result and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        Item={
            'ID': str(result),
            'LatestGreetingTime':now
            })

# return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps(f'Your result is {result}')
    }
