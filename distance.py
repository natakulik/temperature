def MtoF(distance):
    return distance/0.3048

def FtoM(distance):
    return distance*0.3048

def metersOrFeet(dataString):
    if dataString.find('m') != -1:
        temp = int(dataString[0:-1])
        return str(MtoF(temp)) + 'ft'
    elif dataString.find('ft') != -1:
        temp = int(dataString[0:-2])
        return str(FtoM(temp))+'m'