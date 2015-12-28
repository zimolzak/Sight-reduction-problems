from math import sin, cos, asin, acos
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
