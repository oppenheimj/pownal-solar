import relay8 as relays
# relay8 documentation: https://github.com/SequentMicrosystems/relay8-rpi/tree/master/python
from time import sleep

def toggleRelay(relayNum):
    flip = lambda : relays.set(0, relayNum, 0 if relays.get(0, relayNum) else 1)

    flip()
    sleep(0.1)
    flip()

def loadRelayNames():
    relayNames = []

    file = open("./data/relayNames.txt", "r")
    for line in file:
        relayNames.append(line.rstrip())

    return relayNames
