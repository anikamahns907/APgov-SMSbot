import time
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from twilio.rest import Client
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler



app = Flask(__name__)
currentMessage = 'test'
def sendText(message):
    print('sending message')
    account_sid = 'AC65c3a80eeee91f09f5b5dc086594be30' #get SID number
    auth_token = '0fa5bf72afe7b8796385c52fb7ff61cb' #get your auth_token
    client = Client(account_sid, auth_token) 
    body = message
    message = client.messages.create(
    body= body,
    from_='[+][1][8329900263]', 
    to='[+][1][9078021615]')
    print(message.sid)

    
def job_function():
    print('sending message')
    f = open("question.txt", "r", encoding="utf-8")
    for line in f:
        isPresent = False
        print("kaka")
        line = line.split('\n')[0]
        print(line)
        if line == '':
            print('tata')
            continue
        f2 = open("usedQs.txt", "r", encoding="utf-8")
        print('caca')

        for line2 in f2: 
            print("jaja")
            line2 = line2.split('\n')[0]
            if line2 == line:
                isPresent = True

        if (isPresent):
            continue
        else:
            f2.close()
            f2 = open("usedQs.txt", "a", encoding="utf-8")
            f2.write(line + "\n")
            global currentMessage
            currentMessage = line 
            print("yay")
            sendText(line)
            f.close()
            f2.close()
            return True





sched = BackgroundScheduler(daemon=True)
sched.add_job(job_function,'interval',seconds = 5)
sched.start()


def createToken():
    print('sunset')
        # required for all twilio access tokens
    account_sid = 'AC65c3a80eeee91f09f5b5dc086594be30'
    api_key = 'SK0c50fe6ce0d409929bad25e7b92e0927'
    api_secret = 'pJ0cBU90MsYZ3CgHWmPmJmStUH5he9bR'

    # required for Chat grants
    identity = 'anika'

    # Create access token with credentials
    token = AccessToken(account_sid, api_key, api_secret, identity=identity)

    # Create a Video grant and add to token
    video_grant = VideoGrant(room='DailyStandup')
    token.add_grant(video_grant)

    # Return token info as JSON
    print(token.to_jwt())
    return(token.to_jwt())


#This function logs into twilio and then sends
#This function only runs every 30 mins


#This function handles responses
#This function runs only when theres a response (response in the POST setting to webhook /bot)
@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if currentMessage in incoming_msg:
        # return a quote
        msg.body('success genius!')
        responded = True
    if not responded:
        msg.body('Close... try again! Read the message over!')
    return str(resp)
if __name__ == "__main__":
    app.run(use_reloader=False)
