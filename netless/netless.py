import os
from twilio.rest import Client

acc_sid = os.environ["ASID"]
acc_tok = os.environ["ATOK"]

client = Client(acc_sid, acc_tok)

client.messages.create(
    to="+447909248538",
    from_="+447481346184",
    body="Test"
)
