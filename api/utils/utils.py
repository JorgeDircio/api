import smtpd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from smtplib import SMTPResponseException, SMTP

def sendMail(html, subject, to):
    message = MIMEMultipart('alternative')
    message['subject'] = subject
    message['From'] = os.getenv('SMTP_USER')
    message['To'] = to

    message.attach(MIMEText(html, 'html'))

    try:
        server = SMTP(os.getenv('SMPT_HOST'), os.getenv('SMTP_PORT'))
        server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASSWORD'))
        server.sendmail(os.getenv('SMTP_USER'), to, message.as_string())
        server.quit()

    except SMTPResponseException as e:
        print(e)
        