import smtplib
from email.mime.text import MIMEText
from email.header import Header
import config

class EmailSender:
    def __init__(self):
        # creates SMTP session
        self.email_acount = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        self.email_acount.starttls()
        # Authentication
        self.email_acount.login(config.sender, config.authorization_password)



    def send_email(self, message):
        message = MIMEText(message)  # 邮件内容
        message['From'] = Header('never_ever监控器')  # 邮件发送者名字
        message['To'] = Header('想滑雪的小朋友')  # 邮件接收者名字
        message['Subject'] = Header('never_ever可能开始啦！')  # 邮件主题

        # sending the mail
        self.email_acount.sendmail(config.sender, config.receivers, message.as_string())
        # terminating the session
        self.email_acount.quit()

if __name__=="__main__":
    sender = EmailSender()
    sender.send_email("快点快点快醒醒！never ever可能开始啦～\n "
                      "==> https://www.whistlerblackcomb.com/plan-your-trip/ski-and-ride-lessons/never-ever-days.aspx")