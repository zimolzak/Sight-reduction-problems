#!/usr/bin/env python

import ephem
from math import sin, cos, asin, acos

jackson = ephem.Observer()
jackson.lat = '42.2458'
jackson.lon = '-84.4014'
jackson.elevation = 997 # 997 feet. Correct??

jackson.date = '2016/01/12 18:00:00' # 13:00 eastern
s = ephem.Sun(jackson)
print jackson.date, "Alt", s.alt, "Azi", s.az

###

jackson.date = '2016/01/12 19:00:00'
s = ephem.Sun(jackson)
print jackson.date, "Alt", s.alt, "Azi", s.az

jackson.date = '2016/01/12 20:00:00'
s = ephem.Sun(jackson)
print jackson.date, "Alt", s.alt, "Azi", s.az

jackson.date = '2016/01/12 21:00:00'
s = ephem.Sun(jackson)
print jackson.date, "Alt", s.alt, "Azi", s.az

###

print "sun radius", s.radius

print
jackson.date = '2016/01/12 18:00:00' # 13:00 eastern
print "At", jackson.date, "...."

gha = ephem.degrees('87:56.8')
print "GHA", gha
dec = ephem.degrees('-21:38.7')
print "Dec", dec

lha = ephem.degrees(gha + jackson.lon)
print "long", jackson.lon
print "LHA", lha

S = sin(dec)
print "S", S
C = cos(dec) * cos(lha)
print "C", C
