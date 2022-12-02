import smtplib
from email.mime.text import MIMEText
from email.header import Header
import config

class EmailSender:
    def __init__(self):
        pass
    @staticmethod
    def send_email(message, sender_name='never_ever监控器',
                   receiver_name='想滑雪的小朋友', subject= 'never_ever可能开始啦！'):
        """
        :param message: The content of the message
        :param sender_name: Name shew on the sender field
        :param receiver_name: Name shew on the receiver field
        :param subject: Subject of the email
        :return:
        """
        # creates SMTP session
        email_acount = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        email_acount.starttls()

        # Authentication
        email_acount.login(config.sender, config.authorization_password)

        message = MIMEText(message)
        message['From'] = Header(sender_name)
        message['To'] = Header(receiver_name)
        message['Subject'] = Header(subject)

        # sending the mail
        email_acount.sendmail(config.sender, config.receivers, message.as_string())
        # terminating the session
        email_acount.quit()

if __name__=="__main__":
    sender = EmailSender()
    sender.send_email("快点快点快醒醒！never ever可能开始啦～\n "
                      "==> https://www.whistlerblackcomb.com/plan-your-trip/ski-and-ride-lessons/never-ever-days.aspx")