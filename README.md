# Pownal Solar
<img src='docs/images/logo.png' width=196>

# Introduction
This software runs on a raspberry pi and toggles up to eight relays.

# Setup
Begin by cloning the repository
```
$ git clone https://github.com/oppenheimj/pownal-solar.git
```
Modify the contents of `data/*`. Add up to eight relay names in `relayNames.txt` and specify schedules within `times.csv`. For example, if `relayNames.txt` looks like
```
Outside lights
Modem
Kitchen lights
```
and `times.csv` looks like
```
1,0600,2100
3,0200,0500
```
then the outside lights will be toggled at 6am and 9pm and the Kitchen lights at 2am and 5am. Finally, run both
```
$ python scheduler.py 
```
and
```
$ python menu.py
```
as different processes.

# Next steps
- Schedule strict turn-on or turn-off commands, rather than simply toggling
- Add a simple API to allow the relays to be controlled over HTTP on the local network