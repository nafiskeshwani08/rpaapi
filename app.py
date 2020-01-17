import requests
import time

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/snow_request', methods=['POST'])
def snow_request():
    req = request.get_json(silent=True, force=True)
    if req.get("queryResult").get("action") == "input.phonenumber":
        phonenumber = req.get("queryResult").get("parameters").get("phonenumber")
        r = deploybot(phonenumber)
        return r

def CRauth():
    authurl = "https://aa-saleseng-usw2.my.automationanywhere.digital/v1/authentication"
    data = {"Username": "nafis.keshwani","Password": "test1234"}
    data_json = json.dumps(data)
    headers = {'Content-Type':'application/json'}
    response = requests.post(authurl, data=data_json, headers=headers)
    output = response.json()
    token = output['token']
    return token

def deploybot(phonenumber):
    token = CRauth()
    CRurl = "https://aa-saleseng-usw2.my.automationanywhere.digital/v2/automations/deploy"
    data = {"fileId": "34787","runAsUserIds":["1678"],"runWithRdp": "false","botInput":{"vPhoneNumber":{"type": "STRING","string": phonenumber}}}
    data_json = json.dumps(data)
    headers = {'Content-Type':'application/json',"X-Authorization":token}
    response = requests.post(CRurl, data=data_json, headers=headers)
    output = response.json()
    reply = "Your bot has been processed and the phone number will be changed."
    my_result = {
        "fulfillmentText": reply,
        "source": reply
        }
    res = json.dumps(my_result, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == "__main__":
	app.run(debug=True, port=port, host='0.0.0.0')
