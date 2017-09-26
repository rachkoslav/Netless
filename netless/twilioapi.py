from twilio.rest import Client


class SMS:
    def __init__(self, sid, token):
        #if sid or token is None:
            #print "Invalid acc_sid or acc_tok! Exiting..."
            #print sid, token
	    #exit(-1)

        self.acc_sid = sid
        self.acc_tok = token

        self.twilioClient = Client(self.acc_sid, self.acc_tok)

    def send_msg(self, toNum, fromNum, text):
        self.twilioClient.messages.create(
            to=toNum,
            from_=fromNum,
            body=text
        )
