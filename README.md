# Netless
  -- Simple SMS Application

## Prerequisites
Python 2.7 version installed.

---
## Setup
To install the required libraries run the following code from the Netless directory:
`sudo make init`. This will install libs like twilio, Flask and requests, which are crucial for the application to runs and funcions correctly.

---
## Running the application
There are two ways of doing this:
1. Executing `python netless/netless.py &` from the project directory
2. Executing `make run` from the project directory.

The latter one seems to not recording logs which I find strange.

---
## Communication
To initiate contact with the application you have to send SMS to my 'twilio number'(Unfortunately, your phone number must be first approven by the app) and either use a random text or include one of the following keywords:
1. 'JOKE' - returns as a SMS a random Chuck Norris fact or joke(be warned it can return some extreme 'jokes')
2. 'WEATHER' - supposed to give you the weather for Leeds, UK(Not yet implemented) 

---
## Internet Usage
Application requires open `5000` port to be able to communicate with the twilio api.

---
## TODO:
<b>NOTE: This is an one-night project!<b>
1. Weather api to get the weather for specified location
2. Voice interaction(possible but a bit low priority right now)
3. Email api - Send and Receive emails to your phone via text message.
4. Anything you would like to see? 
