
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import uuid


def CreateHashKey(FirstKey,SecoundKey):
    # hash = hashlib.sha256()
    # hash.update(('%s%s' % (FirstKey,SecoundKey)).encode('utf-8'))
    Hashkey = uuid.uuid1()

    return Hashkey

a=CreateHashKey('Namanl494@gmail.com','prashant').hex
K =a[:8]
print(K)    

message = Mail(
    from_email='manyypallive@gmail.com',
    to_emails='prashantgoyal.enthuons@gmail.com',
    subject='DoctorSignup',
    html_content='<strong>Hi,Welcome to our Organization, Your UserId is :"'+str(K)+'"</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
   
    

  

    


except Exception as e:
    print(e)
