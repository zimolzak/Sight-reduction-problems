#!/usr/bin/env python

import ephem
from sr_lib import altazimuth, almanac

datelist = ['2016/01/12 18:00:00', '2016/01/12 19:00:00',
            '2016/01/12 20:00:00', '2016/01/12 21:00:00']

jackson = ephem.Observer()
jackson.lat = '42.2458'
jackson.lon = '-84.4014'
jackson.pressure = 0
jackson.elevation = 303.9 # meters = 997 feet. Doesn't affect sun much.

for i in range(len(datelist)):
    jackson.date = datelist[i]
    s = ephem.Sun(jackson)
    al = almanac(jackson.date)
    aa = altazimuth(al['gha'], al['dec'], jackson.lon, jackson.lat)
    print "Alt", s.alt, "Azi", s.az
    print "    from gha:", aa
    print "    func:", almanac(datelist[i])

print
print "sun radius", s.radius

