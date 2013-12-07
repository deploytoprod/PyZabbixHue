
from zabbixdata import *
from phue import *

while True:

    zdata = ZabbixData()
    zdata.getunacktriggers()
    zdata.getworsttrigger()
    print zdata.worsttrigger

    phue = PHue()
    phue.bootstrap()
    phue.updategroup(0,zdata.worsttrigger)
    phue.pushgroup()

    sleep(10)