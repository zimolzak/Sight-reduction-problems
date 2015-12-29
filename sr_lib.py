from math import sin, cos, tan, asin, acos, pi, sqrt, atan2
import ephem

def altazimuth(gha, dec, long, lat):
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
    """http://shipofficer.com/so/wp-content/uploads/2015/02/17.-Altitude.pdf"""
    assert type(app_alt) == ephem.Angle
    assert app_alt > ephem.degrees('11')
    minutes = 0.96 / tan(app_alt)
    return ephem.degrees((minutes / 60 / 360) * (2 * pi))

def parallax(alt):
    assert type(alt) == ephem.Angle
    HP = ephem.earth_radius / ephem.meters_per_au
    return ephem.degrees(asin(sin(HP) * cos(alt)))

def sd(date):
    assert type(date) == ephem.Date
    return ephem.Sun(date).radius

def ho(ha, date, limb):
    assert limb == 'LL' or limb == 'UL'
    if limb == 'LL':
        semi_diam = sd(date)
    elif limb == 'UL':
        semi_diam = -1 * sd(date)
    return ephem.degrees(ha + parallax(ha) - refraction(ha) + semi_diam)

def minute(x):
    return x / (2*pi) * 360 * 60

def ha(hs, ie, arc, height_m):
    assert arc == 'on' or arc == 'off'
    assert type(hs) == type(ie) == ephem.Angle
    if arc == 'on':
        ie = ephem.degrees(ie * -1)
    dip = ephem.degrees(str(-1.758 / 60 * sqrt(height_m)))
    return ephem.degrees(hs + ie + dip)

def ho2hs(ho, ie, arc, height_m, date_str, limb):
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
    if ho > hc:
        return [ephem.degrees(ho - hc), 'Toward Gp']
    else:
        return [ephem.degrees(hc - ho), 'Away from Gp']

def destination(p1, l1, t, d):
    # p1 phi1 lat. l1 lambda1 long. t theta heading. d angular dist.
    # http://www.movable-type.co.uk/scripts/latlong.html
    # Chris Veness; MIT License
    p2 = asin(sin(p1) * cos(d) + cos(p1) * sin(d) * cos(t))
    l2 = l1 + atan2(sin(t) * sin(d) * cos(p1), cos(d) - sin(p1) * sin(p2))
    dest = ephem.Observer()
    dest.lat = ephem.degrees(p2)
    dest.long = ephem.degrees(l2)
    return dest

def roundup_deg(angle):
    """what do I add to this to make it integer degrees?"""
    dms = str(angle).split(':')
    min_sec_only = ephem.degrees(':'.join(['0', dms[1], dms[2]]))
    if angle < 0:
        return min_sec_only
    return ephem.degrees('1') - min_sec_only

def int_deg(angle):
    dms = str(angle).split(':')
    return ephem.degrees(dms[0])
