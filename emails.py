import smtplib

def sendEmail(email, password, message, email_receptor):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(email, password)
    # server.sendmail("from", "to", "message")
    server.sendmail(email, email_receptor, message)
