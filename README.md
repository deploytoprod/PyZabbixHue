PyZabbixHue
===========

Getting Zabbix triggers on the most fashion way.

Dependencies
------------

This project uses [this](https://github.com/bobeirasa/virtualenvs/tree/master/pyzabbixhue) virtualenv. If you decide to
use the mentioned virtualenv, you don won't need to install those dependencies, but if you like to run this on your
*Domain-0*, you would like to install the dependencies listed below:

  * pip install pyzabbix  *# For querying zabbix API using Python*
  * pip install beautifulhue  *# For make the magic happen*

Limitations
-----------

As this software is OpenSource, I developed it to fit my needs, so there's some things on it that only works on certain
scenarios (mine). If you are expecting problems, please let me know so as I can modify the software and attend you. With
this, the project becomes richer. Also feel free to fork and make pull requests, everything is to everybody!

  * To be more easy to use, PyZabbixHue scans the network for bridges, and uses the first bridge found. So if you have
  more than 1 bridge on your network, PyZabbixHue will use randomly.

Version History
---------------

##### 20131205
  * Inicial public release.