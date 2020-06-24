from twilio.rest import Client 
 
account_sid = 'AC8be886344463be903213a4c125cb5559' 
auth_token = '28dfb96d85c31a09c6b83c42a9af06c5' 
client = Client(account_sid, auth_token) 
def recordatorio():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Ora Prro',      
                              to='whatsapp:+5213318019871' 
                          ) 
 
    print(message.sid)  