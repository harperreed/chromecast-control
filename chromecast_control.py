import requests
import logging
logging.basicConfig(level=logging.INFO)
from BeautifulSoup import BeautifulSoup

"""


Other interesting URLS

http://CHROMECAST_IP:8008/ssdp/device-desc.xml
http://CHROMECAST_IP:8008/apps/ChromeCast
http://CHROMECAST_IP:8008/apps/

"""


class chromecast_control:

    port = "8008"

    def __init__(self, ip, app_id):
        self.ip = ip
        self.app_id = app_id

    def build_url(self):
        self.app_url = 'http://' + self.ip + ':' + self.port + '/apps/' + self.app_id

    def stop(self):
        self.build_url()
        requests.delete(self.app_url)

    def start(self):
        self.build_url()
        r = requests.post(self.app_url)
        print r.text

    def info(self):
        self.build_url()
        r = requests.get(self.app_url)
        #I hate myself. XML is annoying. 
        response=BeautifulSoup(r.text)
        state =  response.service.state.text
        if state == "running":
            try:
                activity = response.find("activity-status").description.text
            except:
                state = "starting"
                activity = "None"
        else:
            activity = None

        return {'state': state, 'activity':activity}


if __name__ == "__main__":

    target_ip = 'CHROMECAST_IP' 
    app_id = 'APPID'
    a = chromecast_control(target_ip, app_id)
    a.start() #start the app on the target chromecast
    print a.info() #get chromecast status
    a.stop() #stop the app on the chromecast
