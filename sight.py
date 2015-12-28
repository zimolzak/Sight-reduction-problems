#!/usr/bin/env python

import ephem
from sr_lib import altazimuth, almanac

datelist = ['2016/01/12 18:00:00', '2016/01/12 19:00:00',
            '2016/01/12 20:00:00', '2016/01/12 21:00:00']

ghalist = [ephem.degrees('87:56.8'), ephem.degrees('102:56.5'),
           ephem.degrees('117:56.3'), ephem.degrees('132:56.0')]

declist = [ephem.degrees('-21:38.7'), ephem.degrees('-21:38.3'),
           ephem.degrees('-21:37.8'), ephem.degrees('-21:38.4')]

jackson = ephem.Observer()
jackson.lat = '42.2458'
jackson.lon = '-84.4014'
jackson.pressure = 0
jackson.elevation = 303.9 # meters = 997 feet. Doesn't affect sun much.

for i in range(len(datelist)):
    jackson.date = datelist[i]
    s = ephem.Sun(jackson)
    aa = altazimuth(ghalist[i], declist[i], jackson.lon, jackson.lat)
    print "Alt", s.alt, "Azi", s.az, 
    print aa
    print "    diffs:", ephem.degrees(s.alt - aa['Hc']), ephem.degrees(s.az - aa['Z'])
    print "    lst:", jackson.sidereal_time()
    print "    ra:", s.ra
    print "    lha:", ephem.degrees(jackson.sidereal_time() - s.ra)
    print "    lha_a:", ephem.degrees(ghalist[i] + jackson.lon)
    gha_ephem = ephem.degrees(jackson.sidereal_time() - s.ra - jackson.lon)
    print "    gha alman:", ghalist[i]
    print "    gha ephem:", gha_ephem
    print "    diff:", ephem.degrees(ghalist[i] - gha_ephem)
    print "    diff dec:", ephem.degrees(s.dec - declist[i])
    print "    dec alm:", declist[i]
    print "    func:", almanac(datelist[i])

print
print "sun radius", s.radius

