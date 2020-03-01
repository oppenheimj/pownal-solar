import csv
from datetime import datetime
from time import sleep
import common

class RelayToggleScheduler(object):
    def __init__(self):
        self.loadSchedule()
        self.today = datetime.today().date()

    def loadSchedule(self):
        self.relayNames = common.loadRelayNames()
        self.schedule = {}

        constructEntry = lambda milTime: {
            'milTime': milTime,
            'timeObject': datetime.strptime(milTime, '%H%M').time(),
            'doneToday': False
        }

        with open('./data/times.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.schedule[int(row[0])] = list(map(lambda milTime: constructEntry(milTime), row[1:]))

    def resetBooleans(self):
        for relayNum in self.schedule:
            for time in self.schedule[relayNum]:
                time['doneToday'] = False

    def detectNewDay(self):
        maybeNewDay = datetime.today().date()

        if maybeNewDay != self.today:
            self.today = maybeNewDay
            self.resetBooleans()

    def checkSchedules(self):
        todayAt = lambda h, m: datetime.now().replace(hour=h, minute=m)

        for relayNum in self.schedule:
            for time in self.schedule[relayNum]:
                if todayAt(time['timeObject'].hour, time['timeObject'].minute) < datetime.now() and not time['doneToday']:
                    print(f'Toggling relay ({relayNum}) "{self.relayNames[relayNum-1]}" at {datetime.now()}')
                    common.toggleRelay(relayNum)
                    time['doneToday'] = True

    def run(self):
        while True:
            sleep(1)
            self.checkSchedules()
            self.detectNewDay()

RelayToggleScheduler().run()
