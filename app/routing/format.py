from datetime import date

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import sender, recipient, password

def newEmail(random_fact: str, fact_of_the_day: str) -> None:
    message = MIMEMultipart()
    message["Subject"] = f"Your Fact of the Day: {date.isoformat(date.today())}"
    message["From"] = sender
    message["To"] = recipient

    payload = f"""\
        <html>
            <h1>Good Morning!</h1>
            <p><b>This is the fact of the day:</b> {fact_of_the_day}</p>
            <p><b>This is a random fact:</b> {random_fact}</p>
        </html>
    """
    message.attach(MIMEText(payload, "html"))

    try:
        with smtplib.SMTP(
            host="smtp.gmail.com",
            port=587
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