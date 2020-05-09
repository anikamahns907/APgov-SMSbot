from twilio.rest import Client
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler



app = Flask(__name__)

#This function logs into twilio and then sends
#This function only runs every 30 mins
currentMessage = ""
def job_function():
    print('sending message')
    # f = open("question.txt", "r")
    # for line in f:
    #     line = line.split('\n')[0]
    #     print(line)
    #     if line == '':
    #         continue
    #     currentMessage = line
    #     f.write(line)
    #     break
    account_sid = 'AC65c3a80eeee91f09f5b5dc086594be30' #get SID number
    auth_token = '153680b34b75a54d2012d9f69d9c9317' #get your auth_token
    client = Client(account_sid, auth_token) 
    message = client.messages.create(
    body= currentMessage,
    from_='[+][1][8329900263]', 
    to='[+][1][9078021615]')
    print(message.sid)




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
    app.run(debug=True)

    sched = BlockingScheduler()
    # Schedule job_function to be called every two hours
    sched.add_job(job_function, 'interval', minutes = 1)
    sched.start()
