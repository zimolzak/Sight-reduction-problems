#!/usr/bin/env python

import ephem
from math import sin, cos, asin, acos

jackson = ephem.Observer()
jackson.lat = '42.2458'
jackson.lon = '-84.4014'
#jackson.elevation = 303.9 # meters = 997 feet.
jackson.elevation = 0 # fixme later

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
#print "GHA", gha
dec = ephem.degrees('-21:38.7')
#print "Dec", dec

## Step 1
lha = ephem.degrees(gha + jackson.lon)
#print "long", jackson.lon
#print "LHA", lha

## Step 2
S = sin(dec)
#print "S", S
C = cos(dec) * cos(lha)
#print "C", C
Hc = ephem.degrees(asin(S * sin(jackson.lat) + C * cos(jackson.lat)))
print "Hc", Hc

## Step 3
X = (S * cos(jackson.lat) - C * sin (jackson.lat)) / cos(Hc)
if X > 1:
    X = 1
elif X < -1:
    X = -1
A = ephem.degrees(acos(X))
#print "A", A

## Step 4
if lha > ephem.degrees('180'):
    Z = ephem.degrees(A)
else:
    Z = ephem.degrees(ephem.degrees('360') - A)
print "Z", Z
