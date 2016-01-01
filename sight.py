#!/usr/bin/env python

import ephem
from sr_lib import (altazimuth, almanac, ha, ho, intercept, destination,
                    ho2hs, roundup_deg, int_deg, ho249, ho_correction,
                    ini_bearing, RefractionError)
from math import pi
import random

n_dates = 3

valid_parameters = False

while not valid_parameters:

    valid_parameters = None
    sights_string = ''
    
    datelist = ['2016/01/12 14:00:00']
    
    #randomize the initial date
    curr_date = ephem.Date(datelist[0])
    days = random.randint(1, 270)
    mins = random.uniform(0, 60)
    datelist[0] = ephem.Date(days + mins * ephem.minute + curr_date)
    
    # Make up some further dates
    while len(datelist) < n_dates:
        prev_date = ephem.Date(datelist[-1])
        elapsed = random.normalvariate(1, (10/60.0) / 2.576)
        curr_date = ephem.Date(elapsed * ephem.hour + prev_date)
        datelist.append(str(curr_date))
    
    # Secret true coordinates
    jackson = ephem.Observer()
    jackson.lat = str(random.uniform(-64,64)) # keep S of Reykjavik
    jackson.lon = str(random.uniform(-180, 180))
    jackson.pressure = 0
    jackson.elevation = 303.9 # meters = 997 feet. Doesn't affect sun much.
    
    ## Set up (random) free parameters
    ie_ref = ephem.degrees(str(random.uniform(0,3) / 60))
    arc_ref = random.choice(['on', 'off'])
    eyeht_ref = round(random.uniform(1,15), 1)
    limb_ref = random.choice(['LL', 'UL', 'LL', 'LL'])
    
    general_direction = ephem.degrees(random.uniform(0, 2*pi))
    
    for date_str in datelist:
    
        ## Pose problem by doing date- and secret-location-specific
        ## back-calculations.
        
        jackson.date = date_str
        refsun = ephem.Sun(jackson) #secret
        try:
            hs_1 = ephem.degrees(0)
            hs_1 = ho2hs(refsun.alt, ie_ref, arc_ref, eyeht_ref,
                         date_str, limb_ref)
            # hs_1 is nonsecret but will let us derive the secret.
        except RefractionError as err:
            print "*** Will need to try again. Sun too low here/now. ***"
            print "\t" + str(err)
            valid_parameters = False
        sights_string += "Problem\n--------\n"
        sights_string += "* Hs " + str(hs_1) + "\n"
        sights_string += ("* IE " + str(ie_ref) + ' ' + arc_ref + " the arc. Eye " +
               str(eyeht_ref) + " meters. Sun " + limb_ref + ".\n")
        dr = jackson.copy() # soon to be non-secret
        dr.lat += ephem.degrees(str(random.normalvariate(0, 1 / 2.576)))
        # 2.576 SD = 99% of all variates (between -1 and 1 deg).
        dr.lon += ephem.degrees(str(random.normalvariate(0, 1 / 2.576)))
        
        ap = dr.copy()
        ap.date = date_str
        sights_string += '* ' + str(ap.date) + " UTC\n"
        sights_string += "* Dead reckoning position " + str(dr.lat) + ' ' + str(dr.lon) + "\n"
        sights_string += "\n"
        
        ## Do sight reduction, to find solution to problem.
        
        sights_string += "Solution\n--------\n"
        ha_1 = ha(hs_1, ie_ref, arc_ref, eyeht_ref)
        try:
            ho_1 = ephem.degrees(0)
            ho_1 = ho(ha_1, ephem.Date(date_str), limb_ref)
        except RefractionError as err:
            print "*** Can't calculate an Ho. Intercept not valid. ***"
            print "\t " + str(err)
            valid_parameters = False
        sights_string += "* Ha " + str(ha_1) + "\n"
        sights_string += "* Ho " + str(ho_1) + "\n"
        al = almanac(date_str)
        sights_string += "* GHA " + str(al['gha']) + " / Dec " + str(al['dec']) + "\n"
        # Choose an AP
        ap.lat = int_deg(dr.lat) # FIXME - more logical to round not int().
        base_ap_lon = int_deg(dr.lon)
        ap.lon = base_ap_lon + roundup_deg(al['gha'])
        sights_string += "* Ass Long " + str(ap.lon) + "\n"
        lha = ephem.degrees(al['gha'] + ap.lon)
        sights_string += "* LHA " + str(lha.norm) + "\n"
        # Solve the triangle, given our AP
        sights_string += "* calculating at AP " + str(ap.lat) + ' ' + str(ap.lon) + "\n"
        s = ephem.Sun(ap)
        sights_string += "* Hc " + str(s.alt) + " / Z " + str(s.az) + "\n"
        # Go from AP to real P
        I = intercept(ho_1, s.alt)
        sights_string += "* Intercept " + str(I[0]) + ' ' + I[1] + "\n"
        if I[1][0] == 'A':
            theta = s.az - pi
        elif I[1][0] == 'T':
            theta = s.az
        x = destination(ap.lat, ap.lon, theta, I[0])
        dir1 = ephem.degrees(s.az - pi/2)
        dir2 = ephem.degrees(s.az + pi/2)
        sights_string +=("* LOP thru " + str(x.lat) + ' ' + str(x.lon) + " in the " + 
              str(dir1.norm) + ' ' + str(dir2.norm) + " direction\n")
        sights_string += "* Z from x to secret " + str(ini_bearing(x, jackson)) + "\n"
        sights_string += "\n"
        
        ## Update the secret coordinates.
        
        heading = ephem.degrees(general_direction +
                   ephem.degrees(str(random.normalvariate(0, 10 / 2.576))))
        distance = random.normalvariate(4.5, 2.5 / 2.576) # nm or min
        d_ang = ephem.degrees('0:' + str(distance))
        new_secret = destination(jackson.lat, jackson.lon, heading, d_ang)
        jackson.lat = new_secret.lat
        jackson.lon = new_secret.lon

    
    if valid_parameters == None:
        valid_parameters = True # should reach only if SR succeeds everywhere.
        print sights_string
    
    print "Was that last set valid? " + str(valid_parameters) + " ----------------"
    print
