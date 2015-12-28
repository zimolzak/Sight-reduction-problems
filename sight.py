#!/usr/bin/env python

import ephem
import math

jackson = ephem.Observer()
jackson.lat = '42.2458'
jackson.lon = '-84.4014'
jackson.elevation = 997 # 997 feet. Correct??
jackson.date = '2016/01/12 18:00:00' # 13:00 eastern

s = ephem.Sun(jackson)

print "Alt", s.alt, "Azi", s.az

###

#jackson.date = '2016/01/12 18:00:00' # 13:00 eastern
