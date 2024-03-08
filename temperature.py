def CtoF(temperature):
    return (9/5)*temperature + 32

def FtoC(temperature):
    return (5/9)*(temperature - 32)

def farenheitOrCelcious(dataString):
    if dataString.find('C') != -1:
        temp = int(dataString[0:-1])
        return str(CtoF(temp)) + 'F'
    elif dataString.find('F') != -1:
        temp = int(dataString[0:-1])
        return str(FtoC(temp))+'C'