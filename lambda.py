import requests
import json

url = "https://api.interakt.ai/v1/public/message/"


def lambda_handler(event,context):
    print(event)
    apikey = event['queryStringParameters']['api']
    mobile = event['queryStringParameters']['mobile']
    visitorName = event['queryStringParameters']['name']
    otp = event['queryStringParameters']['otp']
    try: 
        payload = json.dumps({
        "countryCode": "+91",
        "phoneNumber": mobile,
        "callbackData": "Error message",
        "type": "Template",
        "template": {
            "name": "verificationotp",
            "languageCode": "en",
            "bodyValues": [
            visitorName,
            otp
            ]
        }
        })
        headers = {
        'Authorization': 'Basic '+ apikey,
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return {
             'statusCode': 200,
            'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': str(response.text)
        }
    except:
        return   {
            'statusCode': 200,
            'body': json.dumps('Please Try Again!')
        }
