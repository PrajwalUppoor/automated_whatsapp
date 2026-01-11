from twilio.rest import Client

account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)

def sendmorningmessage():
    message = client.messages.create(
                            from_='whatsapp:+14155238886',
                            body='Good Night ',
                            to='whatsapp:+91'
                           )
    print(message.sid)
