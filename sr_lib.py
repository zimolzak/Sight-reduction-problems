from math import sin, cos, tan, asin, acos, pi, sqrt, atan2
import ephem

def altazimuth(gha, dec, long, lat):
    """Translate Sun's GHA and Dec, plus our position, to Hc and Z.

    Follows the trigonometric procedure in Nautical Almanac.
    """
    ## Step 1
    lha = ephem.degrees(gha + long)
    ## Step 2
    S = sin(dec)
    C = cos(dec) * cos(lha)
    Hc = ephem.degrees(asin(S * sin(lat) + C * cos(lat)))
    ## Step 3
    X = (S * cos(lat) - C * sin (lat)) / cos(Hc)
    if X > 1:
        X = 1
    elif X < -1:
        X = -1
    A = ephem.degrees(acos(X))
    ## Step 4
    if lha > ephem.degrees('180'):
        Z = ephem.degrees(A)
    else:
        Z = ephem.degrees(ephem.degrees('360') - A)
    return dict(Hc=Hc, Z=Z)

def almanac(date):
    """Return the GHA and Dec of the sun for a given date."""
    place = ephem.Observer()
    place.lat = '45.0'
    place.lon = '-90.0'
    place.pressure = 0
    place.date = date
    s = ephem.Sun(place)
    gha_ephem = ephem.degrees(place.sidereal_time() - s.ra - place.lon)
    dec_ephem = ephem.degrees(s.dec)
    return dict(gha=gha_ephem, dec=dec_ephem)

def refraction(app_alt):
    """Calculate atmospheric refraction of a body, given its apparent
    altitude.

    This is part of going from Ha to Ho.

    Source:
    http://shipofficer.com/so/wp-content/uploads/2015/02/17.-Altitude.pdf
    """
    assert type(app_alt) == ephem.Angle
    if app_alt <= ephem.degrees('11'):
        raise RefractionError(ephem.degrees(app_alt))
    minutes = 0.96 / tan(app_alt)
    r = ephem.degrees((minutes / 60 / 360) * (2 * pi))
    return r

def parallax(alt):
    """Calculate parallax of the sun, given its apparent altitude.

    This is part of going from Ha to Ho.
    """
    assert type(alt) == ephem.Angle
    HP = ephem.earth_radius / ephem.meters_per_au
    return ephem.degrees(asin(sin(HP) * cos(alt)))

def sd(date):
    """Return semi-diameter of the sun on a given date.

    This is part (in fact the most significant part) of going from Ha
    to Ho.
    """
    assert type(date) == ephem.Date
    return ephem.Sun(date).radius

def ho(ha, date, limb):
    """Perform altitude correction for a sun sight.

    In other words, translate from Ha to Ho. This does the same that
    the 'yellow sheet' of the Nautical Almanac does.
    """
    assert limb == 'LL' or limb == 'UL'
    if limb == 'LL':
        semi_diam = sd(date)
    elif limb == 'UL':
        semi_diam = -1 * sd(date)
    return ephem.degrees(ha + parallax(ha) - refraction(ha) + semi_diam)

def minute(x):
    """Express an input angle in decimal minutes.

    Useful for debugging things like Hs --> Ha, or Ha --> Ho.
    """
    return x / (2*pi) * 360 * 60

def ha(hs, ie, arc, height_m):
    """Correct a sextant reading for instrument error and eye height.

    In other words, go from Hs to Ho.
    """
    assert arc == 'on' or arc == 'off'
    assert type(hs) == type(ie) == ephem.Angle
    if arc == 'on':
        ie = ephem.degrees(ie * -1)
    dip = ephem.degrees(str(-1.758 / 60 * sqrt(height_m)))
    return ephem.degrees(hs + ie + dip)

def ho2hs(ho, ie, arc, height_m, date_str, limb):
    """Determine sextant reading Hs by back-calculation from Ho and free
    parameters.

    Not much use for 'real' navigation: only for posing navigation
    problems to student. It is worth noting that I DO NOT use proper
    inverse functions of refraction() or parallax(). I use the
    original functions, which results in only an approximation. Sort
    of like saying $100 plus 1% = $101, whereas $101 minus 1% is 99.99
    but close enough for our purposes.
    """
    ## setup
    assert limb == 'LL' or limb == 'UL'
    date = ephem.Date(date_str)
    if limb == 'LL':
        semi_diam = sd(date)
    elif limb == 'UL':
        semi_diam = -1 * sd(date)
    if arc == 'on':
        ie = ephem.degrees(ie * -1)
    dip = ephem.degrees(str(-1.758 / 60 * sqrt(height_m)))
    ## Do back calculations
    ha = ho - parallax(ho) + refraction(ho) - semi_diam # p(ho) and r(ho) appx
    hs = ha - ie - dip
    return ephem.degrees(hs)

def intercept(ho, hc):
    """Calculate intercept by comparing Ho and Hc.

    Simple subtraction. Number of minutes would equal number of
    nautical miles. Function also returns a list telling which
    direction the intercept is relative to Gp (the point on the Earth
    which is directly under the Sun). The function tells you the
    result of the HOMOTO mnemonic, if you will. Intercept is the point
    through which the line of position (LOP, or technically a circle
    of position) passes.
    """
    if ho > hc:
        return [ephem.degrees(ho - hc), 'Toward Gp']
    else:
        return [ephem.degrees(hc - ho), 'Away from Gp']

def destination(p1, l1, t, d):
    """Calculate destination coordinates on the Earth, given start
    coordinates, heading, and (angular) distance.

    p1 is phi_1, which is latitude.
    l1 is lambda_1, which is longitude.
    t is theta, which is heading.
    d is delta, which is angular distance.

    Angular distance is a little tricky but not that much. It works
    fine if you just pass it an ephem.Angle object. A float expressing
    radians will also work. You can use the 1 nm = 1 min trick by
    passing something like ephem.degrees('0:1'), but it should be
    clear that you can't just pass in a float equal to nm or minutes,
    because those aren't the right units. It expects radians, not
    minutes, and 1 min = about 0.0003 radians.)
    """
    # 
    # http://www.movable-type.co.uk/scripts/latlong.html
    # Chris Veness; MIT License
    p2 = asin(sin(p1) * cos(d) + cos(p1) * sin(d) * cos(t))
    l2 = l1 + atan2(sin(t) * sin(d) * cos(p1), cos(d) - sin(p1) * sin(p2))
    dest = ephem.Observer()
    dest.lat = ephem.degrees(p2)
    dest.long = ephem.degrees(l2)
    return dest

def roundup_deg(angle):
    """Answers the question 'What do I add to this angle to make it
    integer degrees?'

    Used for calculating assumed longitude in order to get an integer
    LHA.
    """
    dms = str(angle).split(':')
    min_sec_only = ephem.degrees(':'.join(['0', dms[1], dms[2]]))
    if angle < 0:
        return min_sec_only
    return ephem.degrees('1') - min_sec_only

def int_deg(angle):
    """Return an angle object with only integer degrees."""
    dms = str(angle).split(':')
    return ephem.degrees(dms[0])

def deg(angle):
    """Return a plain integer that is simply degrees extracted."""
    dms = str(angle).split(':')
    return int(dms[0])

def ho249(lat, dec, lha):
    """Determine (uncorrected) Hc and Z from an extremely limited excerpt
    of HO-249.

    In brief, perform a reduction to altitude and azimuth, or solve
    the navigational triangle. Arguments are latitude, declination of
    sun, and LHA (just like HO-249). All of them will be truncated to
    integer degrees (just like HO-249). In any case, you should be
    using an Assumed Latitude, which should be an integer to begin
    which, otherwise you're doing it wrong. Return value is a rather
    bare-bones list [Hc_degrees, Hc_minutes, d, Z, Zn]. 'Little d' is
    one argument you need to enter the correction table, to correct Hc
    for minutes of the body's declination.

    Source is vol. 3 of HO-249, which covers lat 39-89, and decl 0-29.
    """
    H = []
    if (lat < 0 and dec < 0) or (lat > 0 and dec > 0):
        name = 'same'
    else:
        name = 'contrary'
    lat_a = abs(deg(lat))
    dec_a = abs(deg(dec))
    lha_a = deg(lha)
    H = [None, None, None, None]
    if lat_a == 42:
        if name == 'contrary':
            if dec_a == 21: ## page 25
                if lha_a == 4 or lha_a == 356:
                    H = [26, 53, -59, 176]
                elif lha_a == 19 or lha_a == 341:
                    H = [24, 36, -58, 160]
                elif lha_a == 34 or lha_a == 326:
                    H = [19, 36, -54, 146]
                elif lha_a == 49 or lha_a == 360-49:
                    H = [12, 26, -49, 134]
    if H[3] ==  None:
        H.append(None)
        return H
    if lat > 0:
        if lha > pi:
            Zn = H[3]
        else:
            Zn = 360 - H[3]
    else:
        if lha > pi:
            Zn = 180 - H[3]
        else:
            Zn = 180 + H[3]
    H.append(Zn)
    return H

def ho_correction(H, dec):
    """Correct Hc for minutes of declination, from an extremely limited
    excerpt of HO-249.

    Source is table 5 of HO-249. First argument is a bare-bones list
    as described in the ho249() function. From this list we will
    extract uncorrected Hc and 'little d'.
    """
    if H[0] == None or H[1] == None or H[2] == None:
        return None
    Hc = ephem.degrees(str(H[0]) + ':' + str(H[1]))
    d = H[2]
    dms = str(dec).split(':')
    min_dec = int(round(float(dms[1]) + float(dms[2]) / 60.0))
    corr = None
    if abs(d) == 59:
        if min_dec == 39:
            corr = 38
    elif abs(d) == 58:
        if min_dec == 38:
            corr = 37
    elif abs(d) == 54:
        if min_dec == 38:
            corr = 34
    elif abs(d) == 49:
        if min_dec == 38:
            corr = 31
    if d < 0:
        sg = -1
    else:
        sg = 1
    if corr == None:
        return None
    Hc1 = ephem.degrees(Hc + ephem.degrees('0:' + str(corr * sg)))
    return Hc1

def ini_bearing(o, d):
    """Find initial bearing along great circle from origin to destination.

    Uses haversine formula. 
    Adapted from code by Chris Veness.
    github.com/chrisveness/geodesy file latlon.js
    """
    y = sin(d.lon - o.lon) * cos(d.lat)
    x = cos(o.lat) * sin(d.lat) - \
        sin(o.lat) * cos(d.lat) * cos(d.lon - o.lon)
    brng = atan2(y, x)
    return ephem.degrees(brng).norm

class RefractionError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Can't calculate refraction; alt. too low: " + str(self.value)
