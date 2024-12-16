import smtplib

to = input("enter receiver email")
message = input("what message you want to share")
def sendEmail (to, message):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.starttls()
    server.login('senderemail','password')
    server.send('sender',to,message)
    server.close()
sendEmail(to,message)
