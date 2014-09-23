import os
# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

account_sid = str(os.environ.get('SID'))
auth_token = str(os.environ.get('TOKEN'))
dial_from = str(os.environ.get('FROM'))
dial_to = str(os.environ.get('TO'))

client = TwilioRestClient(account_sid, auth_token) 
# Make the call
call = client.calls.create(to=dial_to,
                           from_=dial_from, # Must be a valid Twilio number
                           url="http://reddit-caller.herokuapp.com/")
print call.sid