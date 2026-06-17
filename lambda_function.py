import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def lambda_handler(event, context):

    method = event['requestContext']['http']['method']

    if method == 'GET':

        response = table.scan()

        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }

    elif method == 'POST':

        body = json.loads(event['body'])

        table.put_item(
            Item={
                'noteId': body['noteId'],
                'content': body['content']
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Note inserted successfully!')
        }