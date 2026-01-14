"""
Date: 01/13/2026
Author: Michael Baburyan

Details: 
    - Create email base
    - Attach email base to message using facts
    - Send email through smtp protocol
"""

# used to get the current date in the email subject
from datetime import date

# smtp and email modules
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# env variables
from config import sender, recipient, password, host, port

# create and send new email
def newEmail(random_fact: str, fact_of_the_day: str) -> None:

    # set email headers
    message = MIMEMultipart()
    message["Subject"] = f"Your Fact of the Day: {date.isoformat(date.today())}"
    message["From"] = sender
    message["To"] = recipient

    # initialize body of the email as html
    payload = f"""\
        <html>
            <h1>Good Morning!</h1>
            <p><b>This is the fact of the day:</b> {fact_of_the_day}</p>
            <p><b>This is a random fact:</b> {random_fact}</p>
        </html>
    """

    # attach the html payload 
    message.attach(MIMEText(payload, "html"))

    try:
        # send email using smtp protocol
        with smtplib.SMTP(
            host=host,  # e.g. smtp.gmail.com
            port=port   # e.g. 587
        ) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(user=sender, password=password)
            smtp_server.sendmail(from_addr=sender, to_addrs=recipient, msg=message.as_string())
            smtp_server.quit()
        
        print("Email Sent Succefully!")

    except smtplib.SMTPAuthenticationError:
        raise Exception(f"SMTP Authentication Error, try again...")
    except Exception as e:
        raise Exception(f"SMTP Error: {e}")