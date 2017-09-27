import os
import twilioapi
from jokeapi import getRandomJoke
from weatherapi import getWeatherLeeds
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
import logging

# SMS controller to send separate messages
smsController = twilioapi.SMS(os.environ["ASID"], os.environ["ATOK"])

# Logging code copied from:
# https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('logs.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

netless = Flask(__name__)


@netless.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    respMsg = MessagingResponse()

    # Read body core was partly copied from:
    # https://twilio.radicalskills.com/projects/sms-respond/2.html
    body = request.values.get('Body', None)
    logger.info('The request body: %s' %body)
    if body == 'JOKE':
        respMsg.message(getRandomJoke())
    elif body == 'WEATHER':
        # TODO
        respMsg.message("RAIN!!! (API to be connected)")
    else:
        respMsg.message("You are just waisting my trial credits, aren't you?")

    logger.info('The response: %s' %respMsg)

    return str(respMsg)

if __name__ == '__main__':
    logger.info('App started')
    netless.run(debug=True)
