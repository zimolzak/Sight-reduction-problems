#!/usr/bin/env python

import ephem
from sr_lib import altazimuth, almanac, ha, ho, intercept, destination
from math import pi

datelist = ['2016/01/12 18:00:00', '2016/01/12 19:00:00',
            '2016/01/12 20:00:00', '2016/01/12 21:00:00']

jackson = ephem.Observer()
jackson.lat = '42.2458'
jackson.lon = '-84.4014'
jackson.pressure = 0
jackson.elevation = 303.9 # meters = 997 feet. Doesn't affect sun much.

ap = jackson.copy()
ap.lat = '42'
ap.lon = '-84'

print

for p in [jackson, ap]:
    p.date = datelist[0]
    print p.date, "UTC"
    s = ephem.Sun(p)

    hs_1 = ephem.degrees('25:55:01.2')
    print "hs", hs_1
    ha_1 = ha(hs_1, ephem.degrees('0:1.2'), 'on', 15)
    print "ha", ha_1
    ho_1 = ho(ha_1, ephem.Date(datelist[0]), 'LL')
    print "ho", ho_1
    print "calculating at position", p.lat, p.lon
    print "Hc", s.alt, "/ Z", s.az
    I = intercept(ho_1, s.alt)
    print "Intercept", I
    if I[1][0] == 'A':
        theta = s.az - pi
    elif I[1][0] == 'T':
        theta = s.az
    x = destination(p.lat, p.lon, theta, I[0])
    dir1 = ephem.degrees(s.az - pi/2)
    dir2 = ephem.degrees(s.az + pi/2)
    print "LOP thru", x.lat, x.lon, "in the", dir1.norm, dir2.norm, "direction"
    print
