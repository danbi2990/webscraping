import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")

# def sendMail(subject, body):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = "christmas_alerts@phthonscraping.com"
#     msg['To'] = "danbi2990@gmail.com"
#
#     s = smtplib.SMTP('localhost')
#     s.send_message(msg)
#     s.quit()

bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"), "html.parser")
while bsObj.find("a", {"id":"answer"}).attrs['title'] == "아니요":
    print("It is not Christmas yet.")
    time.sleep(3600)
bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"), "html.parser")
send_email("danbi2990@gmail.com","dnwls1266895","danbi2990@gmail.com","It's Christmas!", "According to https://isitchristmas.com, it is Christmas!")