import os
import twilioapi
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect

# SMS controller to send separate messages
smsController = twilioapi.SMS(os.environ["ASID"], os.environ["ATOK"])

netless = Flask(__name__)


@netless.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    inMsg = MessagingResponse()
    body = inMsg.attrs.get('Body')
    print body

if __name__ == '__main__':
    netless.run(debug=True)
