# import modes
from urllib import request
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading


"""
File:
    network.py

Summary:
    In this Python file, using the free stmp service with our team's email (parsiyamaha@gmail.com), 
    we provided a system so that we can send emails to the user in different parts of the app, including:
    - contact us
    - forget password

    Free stmp service for daily work and this project is the answer. 
    If we have promotional emails (high number of emails), it should be a paid service.
"""


# Function for check internet connection
# ERROR 404 -> [NOT use in project (for now not in fiture)]
def internet_on():
    try:
        request.urlopen('https://github.com/', timeout=1)
        return True
    except request.URLError as err: 
        return False
    

# TEST for send email that has a HTML body
def EMAIL_forget_password_email(new_password:str):
    html_content = '''
<html>
<head>
    <style>
        h1{
            background-color: black;
            color: white;
        }
    </style>
</head>
<body>
    <h1>Hello</h1>
</body>
</html>
'''

    # message.attach(MIMEText(html_content, 'html'))
    return MIMEText(html_content,"html")


# Send simple email (no HTML)
def send_email(_to:str,subject:str,content:list[str,MIMEText],normal_content_bool = True):
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_PASSWORD = "lwne megf lfgh ngbt"
    EMAIL_HOST_USER = "parsiyamaha@gmail.com"
    EMAIL_PORT = 587
    EMAIL_PORT_SSL = 465

    sms = EmailMessage()
    sms["Subject"] = subject
    sms["From"] = EMAIL_HOST_USER
    sms["To"] = _to

    if normal_content_bool :
        sms.set_content(content)
    else :
        sms.attach(content)


    with smtplib.SMTP_SSL(EMAIL_HOST,EMAIL_PORT_SSL) as server :
        server.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
        # server.sendmail(EMAIL_HOST_USER,"iraniparsiya@gmail.com","Hello From Parsiya")
        server.send_message(sms)


# Send email with HTML body
def _send_email_html(_to:str,subject:str,new_password:str):

    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_PASSWORD = "lwne megf lfgh ngbt"
    EMAIL_HOST_USER = "parsiyamaha@gmail.com"
    EMAIL_PORT = 587
    EMAIL_PORT_SSL = 465


    msg = MIMEMultipart("alternative")
    msg["From"] = "parsiyamaha@gmail.com"
    msg["To"] = _to
    msg["Subject"] = subject


    # HTML body text
    html = f"""
<html style="@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');     font-family: 'Poppins', sans-serif;">
<body>
    <div style="background-color: #302c2c; width: 60%; height:100%;">
        <h1 style="color: aqua; font-size: 25px; padding:30px 30px 5px 100px;">Mr.Doctor - Forget password</h1><hr>
        <p style="color: white; padding:20px 30px 30px 30px;">Thank you for using the Mr. doctor app.
            From now on, your password has been changed and you can enter the program only with this password.
            If you are not satisfied with the password, you can use the section: <br>
            <span>User info > Change password </span><br>
            Change your password. <br>
            Of course, this random password has a higher ability to be hacked.</p> 
        <div style="margin-left: 30px;">
            <h1 style="font-size: 25px; color: yellow; padding:25px 30px 0px 50px; border:3px solid aqua;box-shadow: 0 0 .7rem aqua;border-radius:15px; width:50%; height:60px"><span style="color: white;">Password:</span><span style="padding:10px">&nbsp;&nbsp;&nbsp;{new_password}</span></h1><br>
        </div>
        <p style="color: rgb(225, 225, 225); padding:0px 30px 30px 30px;"><span style="font-size: 40px;">⚠️</span>Do not share this password with others to protect your information.</p>
        <div style="padding: 0 0 30px 30px;">
            <a href="https://github.com/parsiya-maha/SMA" style="display: inline-block; text-decoration:none; padding: 1rem 2.8rem;background: aqua;border-radius: .3rem;box-shadow: 0 0 .7rem aqua;font-size: 1rem;color:#302c2c;letter-spacing: .1rem;font-weight: 600;transition: .5s ease;" >More info</a>
        </div>


    </div>
</body>
</html>
"""

    part2 = MIMEText(html, "html")

    msg.attach(part2)

    with smtplib.SMTP_SSL(EMAIL_HOST,EMAIL_PORT_SSL) as server :
        server.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
        server.sendmail(EMAIL_HOST_USER,_to,msg.as_string())


# Send a email with HTML body but with a thread
def send_email_html(_to:str,subject:str,new_password:str):
    thr = threading.Thread(target=_send_email_html,args=[_to,subject,new_password],name="Email sender")
    thr.start()