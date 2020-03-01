import os
import common

def validateInput(userInput):
    global menuOptions

    isInt = lambda x : type(x).__name__ == 'int'
    isInRange = lambda x : 0 < x and x <= len(menuOptions)

    return isInt(userInput) and isInRange(userInput)

def displayMenu():
    global menuOptions

    for i in range(len(menuOptions)):
        print(f'{i+1}) {menuOptions[i]}')

menuOptions = common.loadRelayNames()

while True:
    os.system('clear')
    displayMenu()
    relayNum = int(input('Enter relay number: '))

    if validateInput(relayNum):
        common.toggleRelay(relayNum)
