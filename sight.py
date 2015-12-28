#!/usr/bin/env python

import ephem
from math import sin, cos, asin, acos

datelist = ['2016/01/12 18:00:00', '2016/01/12 19:00:00',
            '2016/01/12 20:00:00', '2016/01/12 21:00:00']

ghalist = []

jackson = ephem.Observer()
jackson.lat = '42.2458'
jackson.lon = '-84.4014'
#jackson.elevation = 303.9 # meters = 997 feet.
jackson.elevation = 0 # fixme later

for d in datelist:
    jackson.date = d
    s = ephem.Sun(jackson)
    print jackson.date, "Alt", s.alt, "Azi", s.az

###

print
print "sun radius", s.radius

print
jackson.date = '2016/01/12 18:00:00' # 13:00 eastern
print "At", jackson.date, "...."

gha = ephem.degrees('87:56.8')
#print "GHA", gha
dec = ephem.degrees('-21:38.7')
#print "Dec", dec

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

print altazimuth(gha, dec, jackson.lon, jackson.lat)
