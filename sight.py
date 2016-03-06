#!/usr/bin/env python

import sys
import ephem
from sr_lib import (altazimuth, almanac, ha, ho, intercept, destination,
                    ho2hs, roundup_deg, int_deg, ho249, ho_correction,
                    ini_bearing, RefractionError)
from math import pi
import random

print """Sun Sight Reduction Practice Problems
========

by Andrew J. Zimolzak

All angles are given in dd:mm:ss (degrees, minutes, seconds) format.
Negative latitude means south, and negative longitude means west. The
assumed position (and LHA, Hc, and Intercept) given in the solution is
just an example. Your AP may not equal the AP that the machine uses,
but yours should ultimately lead you to find a similar celestial
position. That is, after working three sights, compare your calculated
celestial position with the "True (secret) position" of Sight number
3, and you should be close.

"""

n_fixes = 10
sights_per_fix = 3
print_solution = True
flag_2016 = False

for arg in sys.argv:
    if arg == '--no-solutions':
        print_solution = False
    if arg == '--fixed-seed':
        random.seed(10097)
    if arg == '--2016':
        flag_2016 = True

for fix in range(1, n_fixes + 1):

    valid_parameters = False
    
    while not valid_parameters:
    
        valid_parameters = None
        text = '' # A buffer that we print only if no errors occur.
        text += 'Problem number ' + str(fix) + "\n========\n\n"
        if not flag_2016:
            datelist = ['2015/01/12 14:00:00']
        else:
            datelist = ['2016/01/12 14:00:00']
        
        # Randomize the initial date.
        curr_date = ephem.Date(datelist[0])
        days = random.randint(1, 270)
        mins = random.uniform(0, 60)
        datelist[0] = ephem.Date(days + mins * ephem.minute + curr_date)
        
        # Make up some further sight times about an hour apart.
        while len(datelist) < sights_per_fix:
            prev_date = ephem.Date(datelist[-1])
            elapsed = random.normalvariate(1, (10/60.0) / 2.576)
            curr_date = ephem.Date(elapsed * ephem.hour + prev_date)
            datelist.append(str(curr_date))
        
        # Secret true coordinates.
        true = ephem.Observer()
        true.lat = str(random.uniform(-64,64)) # keep S of Reykjavik
        true.lon = str(random.uniform(-180, 180))
        true.pressure = 0
        true.elevation = 303.9 # meters = 997 feet. Doesn't affect sun much.
        
        # Set up the remaining (random) free parameters.
        ie_ref = ephem.degrees(str(random.uniform(0,3) / 60))
        arc_ref = random.choice(['on', 'off'])
        eyeht_ref = round(random.uniform(1,15), 1)
        limb_ref = random.choice(['LL', 'UL', 'LL', 'LL'])
        general_direction = ephem.degrees(random.uniform(0, 2*pi))
        
        for sight_num, date_str in enumerate(datelist):
        
            ## Pose problem by doing date- and secret-location-specific
            ## back-calculations.
    
            # Back-calculate Hs.
            true.date = date_str
            refsun = ephem.Sun(true) #secret
            try:
                hs_1 = ephem.degrees(0)
                hs_1 = ho2hs(refsun.alt, ie_ref, arc_ref, eyeht_ref,
                             date_str, limb_ref)
                # hs_1 is nonsecret but will let student derive the secret.
            except RefractionError as err:
                valid_parameters = False
            text += "Sight number " + str(sight_num + 1) + "\n--------\n"
            text += "* Hs " + str(hs_1) + "\n"
            text += ("* IE " + str(ie_ref) + ' ' + arc_ref +
                              " the arc. Eye " + str(eyeht_ref) +
                              " meters. Sun " + limb_ref + ".\n")
            # Fuzz the secret true coordinates to make DR position.
            dr = true.copy() # soon to be non-secret
            dr.lat += ephem.degrees(str(random.normalvariate(0, 1 / 2.576)))
            # 2.576 SD = 99% of all variates (between -1 and 1 deg).
            dr.lon += ephem.degrees(str(random.normalvariate(0, 1 / 2.576)))
            ap = dr.copy()
            ap.date = date_str
            text += '* ' + str(ap.date) + " UTC\n"
            text += ("* Dead reckoning position " + str(dr.lat) +
                              ' ' + str(dr.lon) + "\n")
            text += "\n"
            
            ## Do sight reduction, to find solution to problem.

            if print_solution:
    
                # Forward-calculate Hs --> Ha --> Ho
                text += "Solution\n--------\n"
                ha_1 = ha(hs_1, ie_ref, arc_ref, eyeht_ref)
                try:
                    ho_1 = ephem.degrees(0)
                    ho_1 = ho(ha_1, ephem.Date(date_str), limb_ref)
                except RefractionError as err:
                    valid_parameters = False
                text += "* Ha " + str(ha_1) + "\n"
                text += "* Ho " + str(ho_1) + "\n"
                # Look up GHA and Dec of the sun.
                al = almanac(date_str)
                text += ("* GHA " + str(al['gha']) + " / Dec " +
                                  str(al['dec']) + "\n")
                # Choose an AP.
                ap.lat = int_deg(dr.lat) # FIXME - better to do round, not int().
                base_ap_lon = int_deg(dr.lon)
                ap.lon = base_ap_lon + roundup_deg(al['gha'])
                text += "* Ass Long " + str(ap.lon) + "\n"
                lha = ephem.degrees(al['gha'] + ap.lon)
                text += "* LHA " + str(lha.norm) + "\n"
                # Solve the triangle (for Hc and Z), given our AP.
                text += ("* Calculating at AP " + str(ap.lat) + ' ' +
                                  str(ap.lon) + ".\n")
                s = ephem.Sun(ap)
                text += "* Hc " + str(s.alt) + " / Z " + str(s.az) + "\n"
                # Go from AP to real position (technically *line* of position).
                I = intercept(ho_1, s.alt)
                text += "* Intercept " + str(I[0]) + ' ' + I[1] + "\n"
                if I[1][0] == 'A':
                    theta = s.az - pi
                elif I[1][0] == 'T':
                    theta = s.az
                x = destination(ap.lat, ap.lon, theta, I[0])
                dir1 = ephem.degrees(s.az - pi/2)
                dir2 = ephem.degrees(s.az + pi/2)
                text +=("* LOP thru " + str(x.lat) + ' ' + str(x.lon) +
                        " in the " + str(dir1.norm) + ' ' + str(dir2.norm) +
                        " direction\n")
                text += ("* Hdg. from Intercept to true position " +
                                  str(ini_bearing(x, true)) + " (Should be "+
                         "similar to LOP.)\n")
                text += ("* True (secret) position is currently " +
                         str(true.lat) + ' ' + str(true.lon) + "\n")
                text += "\n"
            
            ## Update the secret coordinates for next sight.
            
            heading = ephem.degrees(general_direction +
                       ephem.degrees(str(random.normalvariate(0, 10 / 2.576))))
            distance = random.normalvariate(4.5, 2.5 / 2.576) # nm or min
            d_ang = ephem.degrees('0:' + str(distance))
            new_secret = destination(true.lat, true.lon, heading, d_ang)
            true.lat = new_secret.lat
            true.lon = new_secret.lon
    
        if valid_parameters == None:
            valid_parameters = True # happens only if SR succeeds everywhere.
            print text
        elif valid_parameters == False:
            #print "    Guessing new parameters..."
            pass
