#!/usr/bin/env python

import ephem
from sr_lib import (altazimuth, almanac, ha, ho, intercept, destination,
                    ho2hs, roundup_deg, int_deg, ho249, ho_correction)
from math import pi
import random

datelist = ['2016/01/12 18:00:00', '2016/01/12 19:00:00',
            '2016/01/12 20:00:00', '2016/01/12 21:00:00']

# Secret true coordinates
jackson = ephem.Observer()
jackson.lat = '42.2458'
jackson.lon = '-84.4014'
jackson.pressure = 0
jackson.elevation = 303.9 # meters = 997 feet. Doesn't affect sun much.

degree_variate = ephem.degrees(str(random.normalvariate(0, 1 / 2.576)))
# 2.576 SD = 99% of all variates (between -1 and 1 deg).
print degree_variate

## Set up free parameters
ie_ref = ephem.degrees(str(random.uniform(0,3) / 60))
arc_ref = random.choice(['on', 'off'])
eyeht_ref = round(random.uniform(1,15), 1)
limb_ref = random.choice(['LL', 'UL'])

for date_str in datelist:

    ## Set up date- and secret-location-specific back-calculations
    jackson.date = date_str
    refsun = ephem.Sun(jackson) #secret
    hs_1 = ho2hs(refsun.alt, ie_ref, arc_ref, eyeht_ref, date_str, limb_ref)
    print "PROBLEM ----"
    print "Hs", hs_1
    print ("IE " + str(ie_ref) + ' ' + arc_ref + " the arc. Eye " +
           str(eyeht_ref) + " meters. Sun " + limb_ref + '.')
    dr = jackson.copy() # soon to be non-secret
    dr.lat += ephem.degrees(str(random.normalvariate(0, 1 / 2.576)))
    dr.lon += ephem.degrees(str(random.normalvariate(0, 1 / 2.576)))
    
    ap = jackson.copy() # fixme. base on dead reck.
    ap.date = date_str
    print ap.date, "UTC"
    print "Sorta dead reck", dr.lat, dr.lon
    print
    
    ## Do sight reduction
    print "SOLUTION ----"
    ha_1 = ha(hs_1, ie_ref, arc_ref, eyeht_ref)
    ho_1 = ho(ha_1, ephem.Date(date_str), limb_ref)
    print "Ha", ha_1
    print "Ho", ho_1
    al = almanac(date_str)
    print "GHA", al['gha'], "/ Dec", al['dec']
    # AP stuff
    ap.lat = int_deg(jackson.lat)
    base_ap_lon = int_deg(jackson.lon)
    ap.lon = base_ap_lon + roundup_deg(al['gha'])
    print "Ass Long", ap.lon
    lha = ephem.degrees(al['gha'] + ap.lon)
    print "LHA", lha
    # Solve the triangle for AP
    print "calculating at AP", ap.lat, ap.lon
    s = ephem.Sun(ap)
    print "Hc", s.alt, "/ Z", s.az
    H = ho249(ap.lat, al['dec'], lha)
    Hc_final = ho_correction(H, al['dec'])
    print "Hc", Hc_final, "/ Zn", H[4], "(from HO-249!)"
    # Go from AP to real P
    I = intercept(ho_1, s.alt)
    print "Intercept", I
    if I[1][0] == 'A':
        theta = s.az - pi
    elif I[1][0] == 'T':
        theta = s.az
    x = destination(ap.lat, ap.lon, theta, I[0])
    dir1 = ephem.degrees(s.az - pi/2)
    dir2 = ephem.degrees(s.az + pi/2)
    print "LOP thru", x.lat, x.lon, "in the", dir1.norm, dir2.norm, "direction"
    print
