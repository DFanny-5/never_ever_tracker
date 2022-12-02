URL = "https://www.whistlerblackcomb.com/plan-your-trip/ski-and-ride-lessons/never-ever-days.aspx"
from HttpClient import HttpClient
from EmailSender import EmailSender
import time

class NeverEverTracker:
    def __init__(self, web_url, check_time):
        self.web_page = HttpClient(web_url).get_soup()
        self.target_reference = self.web_page.find('div', id="c22_Basic_Content_2")
        self.email = EmailSender()
        self.timer = 0

        self.start_monitroing(check_time) #start the monitor

    def start_monitroing(self, check_time):
        while True:
            new_update = self.web_page.find('div', id="c22_Basic_Content_2")
            time.sleep(check_time)
            if_match = new_update == self.target_reference
            print(f'After {check_time} second, if the content stay unchanged: ', if_match)
            if not if_match:
                self.email.send_email("""Some updates appears on the page: 
                https://www.whistlerblackcomb.com/plan-your-trip/ski-and-ride-lessons/never-ever-days.aspx 
                \n\n 
                Please check it soon""")
                self.target_reference = new_update # update the latest context to avoid duplicate sending


if __name__=="__main__":
    web_soup = NeverEverTracker(URL, 30)
