import boto3
import json
from boto3.dynamodb.conditions import Attr  # 👈 add this import

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Slots')

def lambda_handler(event, context):
    try:
        response = table.scan(
            FilterExpression=Attr('isBooked').eq(False)  # 👈 correct way
        )
        slots = response.get('Items', [])
        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps(slots)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
