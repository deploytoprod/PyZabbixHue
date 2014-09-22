from zabbixdata import *
from phue import *
from time import sleep
from configs import runinterval

phue = PHue()

while True:
    try:
        zdata = ZabbixData()
        zdata.getunacktriggers()
        zdata.getworsttrigger()
        print zdata.worsttrigger

        phue.bootstrap()
        phue.imalive(zdata.worsttrigger)
        phue.updategroup(0,zdata.worsttrigger)
        phue.pushgroup()
    except Exception, e:
        print str(e)
    finally:
        sleep(runinterval)
