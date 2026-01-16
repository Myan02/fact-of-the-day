"""
Date: 01/13/2026
Author: Michael Baburyan

Details: 
    - Create email base
    - Attach email base to message using facts
    - Send email through smtp protocol
"""

from datetime import date

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import sender, recipients, password, host, port


# contains all methods for formatting and sending the email
class Email():

    # initialize email 
    def __init__(self):
        self.message = MIMEMultipart()
    
    # create and send new email
    def createEmail(self, params: dict) -> None:
        # set email headers
        self.message["Subject"] = f"Your Morning Update: {date.isoformat(date.today())}"
        self.message["From"] = sender
        self.message["To"] = ", ".join(recipients)

        # read and format payload as html
        html = open("routing/payload.html", "r", encoding="utf-8")
        payload = html.read().format(**params)
        html.close()

        # attach the html payload 
        self.message.attach(MIMEText(payload, "html"))
    
    def sendEmail(self) -> None:
        try:
            # send email using smtp protocol
            with smtplib.SMTP(
                host=host,  # e.g. smtp.gmail.com
                port=port   # e.g. 587
            ) as smtp_server:
                smtp_server.starttls()
                smtp_server.login(user=sender, password=password)
                smtp_server.sendmail(
                    from_addr=sender, 
                    to_addrs=recipients, 
                    msg=self.message.as_string())
                smtp_server.quit()
            
            print("Email(s) Sent Succefully!")

        except smtplib.SMTPAuthenticationError:
            raise Exception(f"SMTP Authentication Error, try again...")
        except Exception as e:
            raise Exception(f"SMTP Error: {e}")
        