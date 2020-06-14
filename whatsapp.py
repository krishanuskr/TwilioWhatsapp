import os
from twilio.rest import Client

clnt =Client()

from_whatsapp_num='whatsapp:+14155238886'
to_whatsapp_number='whatsapp:' + os.environ['MY_WHATSAPP']

clnt.messages.create(body='Hey Krishanu!', 
                       from_= from_whatsapp_num, 
                       to=to_whatsapp_number)