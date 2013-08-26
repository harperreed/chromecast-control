import requests
import logging
logging.basicConfig(level=logging.INFO)
from BeautifulSoup import BeautifulSoup

"""


"""


class chromecast_control:

    port = "8008"

    def __init__(self, ip, app_id=None):
        self.ip = ip
        self.app_id = app_id

    def build_youtube_url(self):
        return 'http://' + self.ip + ':' + self.port + '/apps/YouTube'

    def build_app_url(self, app_id=None):
        if not app_id:
            app_id = self.app_id
        if not app_id:
            raise Exception("App ID required!")
        return 'http://' + self.ip + ':' + self.port + '/apps/' + app_id

    def stop_app(self, app_id=None):
        requests.delete(self.build_app_url(app_id))

    def start_app(self, app_id=None):
        r = requests.post(self.build_app_url(app_id))
        print r.text

    def info_app(self, app_id=None):
        r = requests.get(self.build_app_url(app_id))
        #I hate myself. XML is annoying.
        response = BeautifulSoup(r.text)
        state = response.service.state.text
        if state == "running":
            try:
                activity = response.find("activity-status").description.text
            except:
                state = "starting"
                activity = "None"
        else:
            activity = None

        return {'state': state, 'activity': activity}

    #Youtube handling

    def stop_youtube(self):
        self.build_youtube_url()
        requests.delete(self.build_youtube_url())

    def start_youtube(self, video_id, t):
        payload = {'v': video_id, 't': t}
        requests.post(self.build_youtube_url(), data=payload)


if __name__ == "__main__":

    target_ip = '192.168.1.4'
    app_id = 'app id from googs'
    a = chromecast_control(target_ip)
    #a.start_app(app_id)
    #a.start_app(app_id)
    #a.start_youtube('awMIbA34MT8', 100)  # start the app on the target chromecast
    #a.stop_youtube()
    #print a.info() #get chromecast status
    #a.stop() #stop the app on the chromecast
