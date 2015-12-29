from math import tan, asin, sin, cos, pi
import ephem

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
        semi_diam = sd(dt)
    elif limb == 'UL':
        semi_diam = -1 * sd(dt)
    return ephem.degrees(parallax(ha) - refraction(ha) + semi_diam)

dt = ephem.Date('2016/05/24 12:00:00')

print dt

for h in range(20, 60):
    ha = ephem.degrees(str(h))
    print h, ho(ha, dt, 'UL')
