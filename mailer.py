import io
import csv
import smtplib
from email.mime.text import MIMEText

# email credentials
email_user = 'somegmailaddress@gmail.com'
email_pw = 'password'

# open file with encoding
file = io.open('msg.txt', mode='r', encoding='utf-8')
msg = MIMEText(file.read())
msg['Subject'] = 'Mass Mailer'
msg['From'] = email_user
# gmail smtp setup & login
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(email_user, email_pw)
# go through list of addresses
address = csv.reader(open('addresses.csv', 'r'))
for row in address:
    del msg['To']
    msg['To'] = row[1]
    try:
        server.sendmail(email_user, [row[1]], msg.as_string())
    except smtplib.SMTPException:
        print("Error")
server.quit()
