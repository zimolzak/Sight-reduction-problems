#!/usr/bin/env python

import ephem
from sr_lib import altazimuth

datelist = ['2016/01/12 18:00:00', '2016/01/12 19:00:00',
            '2016/01/12 20:00:00', '2016/01/12 21:00:00']

ghalist = [ephem.degrees('87:56.8'), ephem.degrees('102:56.5'),
           ephem.degrees('117:56.3'), ephem.degrees('132:56.0')]

declist = [ephem.degrees('-21:38.7'), ephem.degrees('-21:38.3'),
           ephem.degrees('-21:37.8'), ephem.degrees('-21:38.4')]

jackson = ephem.Observer()
jackson.lat = '42.2458'
jackson.lon = '-84.4014'
jackson.elevation = 0 # fixme later
#jackson.elevation = 303.9 # meters = 997 feet.

for i in range(len(datelist)):
    jackson.date = datelist[i]
    s = ephem.Sun(jackson)
    print "Alt", s.alt, "Azi", s.az, 
    print altazimuth(ghalist[i], declist[i], jackson.lon, jackson.lat)

print
print "sun radius", s.radius
