import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import credential as c

def send_email(subject, body, to_email):

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = c.gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Create the server object
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login credentials for sending the mail
    server.login(c.gmail_user, c.app_password)

    # Send the message via the server
    text = msg.as_string()
    server.sendmail(c.gmail_user, to_email, text)

    # Close the server
    server.quit()

    print("Email sent successfully")

# Usage
send_email("Hello", "This is a test email", "utilmonn@gmail.com")
