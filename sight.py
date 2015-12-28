#!/usr/bin/env python

import ephem
import math

s = ephem.Sun()
s.compute()

print "now"
print "RA", s.ra, "Dec", s.dec

for h in range(24):
    d = ephem.Date(42380 + h / 24.0) #2016/1/12 12:00:00
    print d,
    s.compute(d)
    print "RA", s.ra / (2 * math.pi) * 360 , "Dec", s.dec
    print "                  ", "RA", s.a_ra / (2 * math.pi) * 360 , "Dec", s.a_dec
    print "                  ", "RA", s.g_ra / (2 * math.pi) * 360 , "Dec", s.g_dec
