#!/usr/local/bin/python3

import sys
from datetime import datetime, timedelta
import ephem
import math

def sign(x):
    if x >=0:
        return 1
    return -1

# The angle the sun makes with the celestial meridian,
# normalized to [-90, 90]
def norm_az(sun):
    deg = math.degrees(sun.az)
    if deg > 90 and deg < 270:
        deg = deg - 180
    if deg > 270:
        deg = deg - 360
    return deg

# Given a UTC offset and whether or not the place obeys DST,
# yield noon times of each day in UTC
#
# We could use datetime's timezone functionality but DST is tricky
# and ephem does not respect datetime's timezone field anyway
def dst_noon_iterator(offset, dst):
    start = datetime(2018, 1, 1, 12 + offset, 0, 0)
    n = 0
    for n in range(0, 365): # ignoring leap years, high noon won't be in december anyway
        if dst and n >= 69 and n < 307: # March 11, Nov 4
            yield start + timedelta(days=n, hours=-1)
        else:
            yield start + timedelta(days=n)

# Bounds of longitudes
STATES = [
    ("CA", 118.5, 114.6, 8, True),
    ("AZ", 114.5, 109., 7, False),
    ("NM", 109., 103., 7, True),
    ("TX", 103., 100., 6, True), # only the panhandle
    ("OK", 100., 94.5, 6, True),
]


print("STATE", "TIME\t\t", "°W", "12:00:00\t", "12:00:01\t", "11:59:59", sep="\t")

# Is it high noon on `date` with the sun `angle` degrees
# off the meridian?
def check(obs, date, angle):
    # calculate angle against meridian at 12:00:01
    obs.date = date + timedelta(seconds=1)
    sun.compute(obs)
    d1 = norm_az(sun)
    # calculate angle against meridian at 11:59:59
    obs.date = date + timedelta(seconds=-1)
    sun.compute(obs)
    d2 = norm_az(sun)
    # are both of these further from the meridian than `angle`?
    if abs(d1) > abs(angle) and abs(d2) > abs(angle):
        print(state, date, abs(lon), angle, d1, d2, sep="\t")

obs = ephem.Observer()
sun = ephem.Sun()
# The latitude does change the azimuthal angles, but it should not affect
# when high noon is. However, I'm picking 35.2 since it's the latitude of
# most of route 66
obs.lat = 35.2

for (state, start, end, offset, dst) in STATES:
    for scaled_long in range(int(start * 100), int(end * 100), -1):
        # Our longitudes are west, so negative
        lon = -scaled_long / 100.
        obs.lon = lon
        prev = None
        for date in dst_noon_iterator(offset, dst):
            obs.date = date
            sun.compute(obs)
            angle = norm_az(sun)

            if prev:
                prev_angle, prev_date = prev
                # filter out cases where the position of clock noon did not flip to the other
                # side of the meridian. This check can be omitted, it exists for efficiency
                if sign(prev_angle) != sign(angle) and abs(prev_angle - angle) < 90:
                    # was it high noon at clock noon yesteray?
                    check(obs, prev_date, prev_angle)
                    # is it high noon at clock noon today?
                    check(obs, date, angle)
            prev = (angle, date)

            