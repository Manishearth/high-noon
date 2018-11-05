#!/usr/local/bin/python

import sys
from datetime import datetime, time, timedelta, date
import ephem
import pytz
import math

# 
EPSILON=0.00418

def sign(x):
    if x >=0:
        return 1
    return -1

def norm_az(sun):
    deg = math.degrees(sun.az)
    if deg > 90 and deg < 270:
        deg = deg - 180
    if deg > 270:
        deg = deg - 360
    return deg

def dst_noon_iterator(offset, dst):
    start = datetime(2018, 1, 1, 12 + offset, 0, 0)
    n = 0
    for n in range(0, 365): # ignoring leap years, high noon won't be in december anyway
        if dst and n >= 69 and n < 307: # March 11, Nov 4
            yield start + timedelta(days=n, hours=-1)
        else:
            yield start + timedelta(days=n)


# 111.8
start = datetime(2018, 1, 1, 19, 0, 0) # noon in GMT + 7
obs = ephem.Observer()
obs.lat = 35.2 # doesn't matter for high noon
sun = ephem.Sun()


for l10 in range(11450, 10900, -1):
    lon = l10 / 100.
    obs.lon = lon
    prev=None
    for d in (start + timedelta(days=n) for n in range(365)):
        obs.date = d
        sun.compute(obs)
        deg = norm_az(sun)

        if prev:
            if sign(prev) != sign(deg) and abs(prev - deg) < 90:
                obs.date = d + timedelta(seconds=1)
                sun.compute(obs)
                d1 = norm_az(sun)
                obs.date = d + timedelta(seconds=-1)
                sun.compute(obs)
                d2 = norm_az(sun)
                if abs(d1) > abs(prev) or abs(d2) > abs(prev):
                    print(d + timedelta(days=-1), lon, prev, d1, d2)
                if abs(d1) > abs(deg) or abs(d2) > abs(deg):
                    print(d, lon, deg, d1, d2)
        prev = deg

        