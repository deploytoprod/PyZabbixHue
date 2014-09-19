from zabbixdata import *
from phue import *
import time

phue = PHue()

while True:

    zdata = ZabbixData()
    zdata.getunacktriggers()
    zdata.getworsttrigger()
    print zdata.worsttrigger

    phue.bootstrap()
    phue.imalive(zdata.worsttrigger)
    phue.updategroup(0,zdata.worsttrigger)
    phue.pushgroup()

    sleep(60)
