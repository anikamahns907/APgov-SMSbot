import json
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from twilio.rest import Client
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def createToken():
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
    print(type(token.to_jwt()))

    realToken = str(token.to_jwt())
    realToken = realToken.split('.')[-1]
    # print(realToken)
    return(realToken)




def job_function():
    print('sending message')
    account_sid = 'AC65c3a80eeee91f09f5b5dc086594be30' #get SID number
    auth_token = createToken()
    client = Client(account_sid, auth_token) 
    message = client.messages.create(
    body='Time for your daily training POOP!',
    from_='[+][1][8329900263]', 
    to='[+][1][9078021615]'
    )
    print(message.sid)

job_function()


# f = open("question.txt", "r")
# wrong = True
# for line in f:
#     line = line.split('\n')[0]
#     print(line)


#     while(wrong):
#         response = input("Copy this text: ")
#         print(response, line)
#         if (str(response) == str(line)):
#             print('success')
#             break
#         else:
#             print('fail')
           


# from twilio.rest import Client
# from flask import Flask, request
# import requests
# from twilio.twiml.messaging_response import MessagingResponse
# from datetime import datetime
# from apscheduler.schedulers.blocking import BlockingScheduler



# app = Flask(__name__)

# #This function logs into twilio and then sends
# #This function only runs every 30 mins
# currentMessage = ""
# def job_function():
#     print('sending message')
#     # f = open("question.txt", "r")
#     # for line in f:
#     #     line = line.split('\n')[0]
#     #     print(line)
#     #     if line == '':
#     #         continue
#     #     currentMessage = line
#     #     f.write(line)
#     #     break
#     account_sid = 'AC65c3a80eeee91f09f5b5dc086594be30' #get SID number
#     auth_token = '0fa5bf72afe7b8796385c52fb7ff61cb' #get your auth_token
#     client = Client(account_sid, auth_token) 
#     message = client.messages.create(
#     body= currentMessage,
#     from_='[+][1][8329900263]', 
#     to='[+][1][9078021615]')
#     print(message.sid)




# #This function handles responses
# #This function runs only when theres a response (response in the POST setting to webhook /bot)
# @app.route('/bot', methods=['POST'])
# def bot():
#     incoming_msg = request.values.get('Body', '').lower()
#     resp = MessagingResponse()
#     msg = resp.message()
#     responded = False
#     if currentMessage in incoming_msg:
#         # return a quote
#         msg.body('success genius!')
#         responded = True
#     if not responded:
#         msg.body('Close... try again! Read the message over!')
#     return str(resp)
# if __name__ == "__main__":
#     app.run(debug=True)

#     sched = BlockingScheduler()
#     # Schedule job_function to be called every two hours
#     sched.add_job(job_function, 'interval', minutes = 1)
#     sched.start()




