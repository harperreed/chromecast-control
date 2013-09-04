#!/usr/bin/python

import logging
import optparse
import requests
import sys

from BeautifulSoup import BeautifulSoup

"""Control a chromecast with python"""


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


def main(argv):
    logging.basicConfig(level=logging.INFO)

    parser = optparse.OptionParser('%prog [options] <server>')
    parser.add_option('-y', '--youtube',
                      help='Play YouTube clip with specified id (use "stop" to stop)')
    parser.add_option('-s', '--status', default=False, action='store_true',
                      help='Show current Chromecast status')
    (options, args) = parser.parse_args(argv)

    if len(args) != 1:
        parser.error('need exactly one argument -- the server')

    target_ip = args[0]
    app_id = 'app id from googs'
    a = chromecast_control(target_ip)

    if options.youtube:
        if options.youtube == 'stop':
            a.stop_youtube()
        else:
            a.start_youtube(options.youtube, 100)

    if options.status:
        # get chromecast status
        print a.info_app()


if __name__ == "__main__":
    main(sys.argv[1:])
