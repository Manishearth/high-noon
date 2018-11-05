#!/usr/local/bin/python

import sys
from datetime import datetime, time, timedelta
import ephem
import math

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

STATES = [
    ("CA", 118.5, 114.6, 8, True),
    ("AZ", 114.5, 109., 7, False),
    ("NM", 109., 103., 7, True),
]


print("STATE", "DATE\t\t", "°", "12:00:00\t", "12:00:01\t", "11:59:59", sep="\t")


def check(obs, d, deg):
    obs.date = d + timedelta(seconds=1)
    sun.compute(obs)
    d1 = norm_az(sun)
    obs.date = d + timedelta(seconds=-1)
    sun.compute(obs)
    d2 = norm_az(sun)
    if abs(d1) > abs(deg) and abs(d2) > abs(deg):
        print(state, d, lon, deg, d1, d2, sep="\t")

for (state, start, end, offset, dst) in STATES:
    obs = ephem.Observer()
    obs.lat = 35.2 # doesn't matter for high noon
    sun = ephem.Sun()


    for scaled_long in range(int(start * 100), int(end * 100), -1):
        lon = -scaled_long / 100.
        obs.lon = lon
        prev=None
        for date in dst_noon_iterator(offset, dst):
            obs.date = date
            sun.compute(obs)
            angle = norm_az(sun)

            if prev:
                prev_angle, prev_date = prev
                if sign(prev_angle) != sign(angle) and abs(prev_angle - angle) < 90:
                    check(obs, prev_date, prev_angle)
                    check(obs, date, angle)
            prev = (angle, date)

            