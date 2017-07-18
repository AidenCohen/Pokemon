import random
import smtplib

sender = 'acohen@sjnma.org'
receivers = ['aidencohen31@gmail.com']
random1  = ["a","b","c","d","e","f","g","h","i","j","k","l", "o" ,"m", "p" ,"q","r","s", "t" ,"u" , "v" ,"w", "x", "y", "z","1","2","3","4","5","6","7","8","9","0"]
def aiden:
    for x in range(11):
        random.randint(0,35)
        y = []
        y.append(x)
message = """From: From Person <????>
To: To David Gold <dgold@sjnma.org>
Subject: This is an email bot

You will be spammed 24/7
"""
aiden()
try:
   smtpObj = smtplib.SMTP('localhost')

    while True:
        time.sleep(600)
        smtpObj.sendmail(sender, receivers, message)
    while True:
        time.sleep(172800)
        random2 = random1[y[0]] +  random1[y[1]] + random1[y[2]]  + random1[y[3]]  + random1[y[4]]  + random1[y[5]]  + random1[y[6]]  + random1[y[7]]  + random1[y[8]]  + random1[y[9]]  + random1[y[10]] 
        sender = random2 + '@gmail.com'
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
   
