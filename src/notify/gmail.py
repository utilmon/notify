import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from . import credential as c


def create_message(receiver_email, subject, message_body):

    # Create message container
    msg = MIMEMultipart()
    msg["From"] = c.gmail_user
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(message_body, "plain"))

    return msg.as_string()


def send_email(to_email, subject, body):

    msg = create_message(to_email, subject, body)

    # Create the server object
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Login credentials for sending the mail
    server.login(c.gmail_user, c.app_password)

    # Send the message via the server
    server.sendmail(c.gmail_user, to_email, msg)

    # Close the server
    server.quit()


def send_strmsg(title="Python Alert", msg: str = "Alert Body"):
    send_email(to_email="utilmonn@gmail.com", subject=title, body=msg)


def test():
    send_strmsg("test", "test_body")


if __name__ == "__main__":
    test()
