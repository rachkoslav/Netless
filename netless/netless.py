import os
import twilioapi
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
import logging

# SMS controller to send separate messages
smsController = twilioapi.SMS(os.environ["ASID"], os.environ["ATOK"])

logger = logging.getLogger(__name__)
hdlr = logging.FileHandler('sample.log')

formatter = logging.Formatter('%(asctime)s %(message)s')
hdlr.setFormatter(hdlr)

hdlr.setLevel(logging.INFO)
logger.addHandler(hdlr)

netless = Flask(__name__)


@netless.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    inMsg = MessagingResponse()
    logger.info(inMsg.to_xml())
    inMsg.message("Response is here!")
    logger.info(str(inMsg))
    return str(inMsg)

if __name__ == '__main__':
    logger.info('First log')
    netless.run(debug=True)
