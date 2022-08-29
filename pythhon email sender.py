import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# import pandas as pd

# change these as per use
your_email = "email"
your_password = "pass"

# recipient email
email = "recipient email"

# establishing connection with gmail
server = smtplib.SMTP_SSL("your smtp-host url", port)
server.ehlo()
server.login(your_email, your_password)

# the message to be emailed
html = """\
		# Import your email tamplete
"""

# Eamil Content
msg = MIMEMultipart('alternative')
msg['Subject'] = "subject"
msg['From'] = your_email
msg['To'] = email

body = MIMEText(html, 'html')
msg.attach(body)

# sending the email
server.sendmail(your_email, email, msg.as_string())

# close the smtp server
server.close()
print("email send success")
