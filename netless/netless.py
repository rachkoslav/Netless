import os
import twilioapi
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
import logging

# SMS controller to send separate messages
smsController = twilioapi.SMS(os.environ["ASID"], os.environ["ATOK"])

# Logging code copied from:
# https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

netless = Flask(__name__)


@netless.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    inMsg = MessagingResponse()
    logger.info(inMsg.to_xml())
    inMsg.message("Response is here!")
    logger.info(str(inMsg))
    return str(inMsg)

if __name__ == '__main__':
    logger.info('App started')
    netless.run(debug=True)
