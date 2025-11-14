import json

def lambda_handler(event, context):
    # TODO implement
    print("presnt from code build")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
