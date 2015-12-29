#!/usr/bin/env python

import ephem
from sr_lib import altazimuth, almanac, ha, ho

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

for p in [jackson, ap]:
    p.date = datelist[1]
    s = ephem.Sun(p)
    al = almanac(p.date)
    aa = altazimuth(al['gha'], al['dec'], p.lon, p.lat)
    print "PyEphem                     Hc ", s.alt, "    Z", s.az
    print " almanac and altazimuth:", aa

hs_1 = ephem.degrees('26')
print "hs", hs_1
ha_1 = ha(hs_1, ephem.degrees('0:1.2'), 'on', 15)
print "ha", ha_1
ho_1 = ho(ha_1, ephem.Date(datelist[0]), 'LL')
print "ho", ho_1
