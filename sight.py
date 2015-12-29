#!/usr/bin/env python

import ephem
from sr_lib import altazimuth, almanac, ha, ho, intercept, destination, ho2hs
from math import pi
import random

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

jackson.date = datelist[0]
refsun = ephem.Sun(jackson)
ie_ref = ephem.degrees('0:1.2')
arc_ref = random.choice(['on', 'off'])
eyeht_ref = 15
limb_ref = 'LL'

print "IE", ie_ref, arc_ref, "the arc. Eye", eyeht_ref, "meters. Sun", limb_ref
print

hs_1 = ho2hs(refsun.alt, ie_ref, arc_ref, eyeht_ref, datelist[0], limb_ref)
ha_1 = ha(hs_1, ie_ref, arc_ref, eyeht_ref)
ho_1 = ho(ha_1, ephem.Date(datelist[0]), limb_ref)
print "hs", hs_1
print "ha", ha_1
print "ho", ho_1
print

for p in [jackson, ap]:
    p.date = datelist[0]
    print p.date, "UTC"
    s = ephem.Sun(p)

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
    
