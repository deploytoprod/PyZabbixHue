'''
This class is responsible for going on Zabbix and get some data
'''

from pyzabbix import ZabbixAPI
import configs

class ZabbixData:
    def __init__(self):
        self.zapi = ZabbixAPI(configs.zabbixapiurl)
        self.zapi.login(configs.zabbixapilogin, configs.zabbixapipasswd)

    def getunacktriggers(self):
        self.triggers = self.zapi.trigger.get(only_true=1,
                                              skipDependent=1,
                                              monitored=1,
                                              active=1,
                                              output='extend',
                                              expandDescription=1,
                                              expandData='host',
                                              withLastEventUnacknowledged=1,
                                              sortfield='priority',
                                              sortorder='DESC'
                                             )

    def getworsttrigger(self):
        tr = []
        #print self.triggers
        if not len(self.triggers):
            self.worsttrigger = -1
            return
        for trigger in self.triggers:
            tr.append(trigger['priority'])

        self.worsttrigger = max(map(int,tr))