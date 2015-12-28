#!/usr/bin/env python

import ephem
from math import sin, cos, asin, acos

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

def altazimuth(gha, dec, long, lat):
    ## Step 1
    lha = ephem.degrees(gha + long)
    ## Step 2
    S = sin(dec)
    C = cos(dec) * cos(lha)
    Hc = ephem.degrees(asin(S * sin(lat) + C * cos(lat)))
    ## Step 3
    X = (S * cos(lat) - C * sin (lat)) / cos(Hc)
    if X > 1:
        X = 1
    elif X < -1:
        X = -1
    A = ephem.degrees(acos(X))
    ## Step 4
    if lha > ephem.degrees('180'):
        Z = ephem.degrees(A)
    else:
        Z = ephem.degrees(ephem.degrees('360') - A)
    return dict(Hc=Hc, Z=Z)

for i in range(len(datelist)):
    jackson.date = datelist[i]
    s = ephem.Sun(jackson)
    print jackson.date, "Alt", s.alt, "Azi", s.az
    print altazimuth(ghalist[i], declist[i], jackson.lon, jackson.lat)

print
print "sun radius", s.radius
