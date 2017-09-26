import os
import twilioapi
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
import logging

# SMS controller to send separate messages
smsController = twilioapi.SMS(os.environ["ASID"], os.environ["ATOK"])

logger = logging.getLogger('netless')
hdlr = logging.FileHandler('logs.log')
formatter = logging.Formatter('%(asctime)s %(message)s')
hdlr.setFormatter(hdlr)
logger.addHandler(hdlr)

netless = Flask(__name__)


@netless.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    inMsg = MessagingResponse()
    body = inMsg.attrs.get('Body')
    logger.info(body)

if __name__ == '__main__':
    netless.run(debug=True)
