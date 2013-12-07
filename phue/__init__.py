from beautifulhue.api import *
from configs import *
from time import sleep
from helpers import *

class PHue:
    def __init__(self):
        phuebridgeip = Portal().get()['resource'][0]['internalipaddress']
        self.bridge = Bridge(device={'ip':phuebridgeip}, user={'name':bridgepasswd})
        self.resource = {}

    def bootstrap(self):

        conf = self.bridge.config.get({'which':'system'})
        try:
            conf['resource'][0]['error']
        except KeyError:
            userexists = True
        else:
            userexists = False


        if not userexists:
            print "First run detected. Press the bridge button now and wait..."
            sleep(10)
            self.config.create({'user':{"devicetype": "PyZabbixHue", "name": bridgepasswd}})

    def updategroup(self,gid,color):
        data = {}
        action = {}
        resource = {}
        if color == -1:
            power = False
        else:
            power = True

        xy = severity2color(color)

        resource['which'] = gid

        action['on'] = power
        action['xy'] = xy
        action['bri'] = 255
        action['sat'] = 255

        data['action'] = action

        resource['data'] = data

        self.resource = resource

    def pushgroup(self):
        self.bridge.group.update(self.resource)