
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='manyypallive@gmail.com',
    to_emails='prashantgoyal494@gmail.com',
    subject='DoctorSignup',
    html_content='<strong>Hi,Welcome to our Organization</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)