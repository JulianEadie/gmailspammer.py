import smptplib, ssl
import spammer

def SendEmail(message)
    smtp_server = "smtp.gmail.com"
    port = "586"
    sender_email = import email.py
    password = import password.py
    receiver_email = import receiver_email.py
    
    context = ssl.creat_default_context()
    
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo
        server.starttls(context=context)
        server.ehlo
        server.login(sender_email, password)
        server.sendemail( sender_email, receiver_email, message)
        
    except Exception as e:
        print(e)
      finally:
        server.quit()
        
text = text.txt
sendemail(txt)
    
