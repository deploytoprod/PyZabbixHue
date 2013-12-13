import configs
import time
import datetime

def severity2color(sev):
    if sev == 5:
        return configs.red
    if sev == 4:
        return configs.orange
    if sev == 3 or sev == 2:
        return configs.yellow
    if sev == 1 or sev == 0 or sev == -1:
        return configs.white