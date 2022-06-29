import flask
from flask import request
import requests
import json

app = flask.Flask(__name__)
url = "https://api.interakt.ai/v1/public/message/"

@app.route('/', methods = ['GET'])
def home():
    token = str(request.args['token'])
    mobile = str(request.args['mobile'])
    visitorName = str(request.args['name'])
    otp = str(request.args['otp'])
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
        'Authorization': 'Basic '+ token,
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text
    except:
        return  "Error Message"
