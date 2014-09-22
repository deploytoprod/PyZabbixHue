def severity2color(sev):
    red = [0.674,0.322]
    orange = [0.700,0.400]
    yellow = [0.700, 0.500]
    white = [0.350,0.350]
    green = [0.408,0.517]
    sevMap = {5:red, 4:orange, 3:yellow, 2:yellow, 1:white, 0:white, -1:white, -2:green}
    return sevMap[sev]
