URL = "https://www.whistlerblackcomb.com/plan-your-trip/ski-and-ride-lessons/never-ever-days.aspx"
from HttpClient import HttpClient
from EmailSender import EmailSender
import time
from datetime import datetime


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

            if_match = new_update == self.target_reference
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f'After {check_time} second, if the content stay unchanged: ', if_match, f' @ {current_time}')
            if not if_match:
                self.email.send_email("""Some updates appears on the page: \nhttps://www.whistlerblackcomb.com/plan-your-trip/ski-and-ride-lessons/never-ever-days.aspx\n\nPlease check it soon""")

                # update the latest context to avoid duplicate sending
                self.target_reference = new_update
            time.sleep(check_time)


if __name__=="__main__":
    web_soup = NeverEverTracker(URL, 30)
