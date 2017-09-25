import os
from twilio.rest import Client

acc_sid = os.environ["TASID"]
acc_tok = os.environ["TATOK"]

client = Client(acc_sid, acc_tok)

client.messages.create(
    to="+7909248538",
    from_="+447481346184",
    body="Test"
)