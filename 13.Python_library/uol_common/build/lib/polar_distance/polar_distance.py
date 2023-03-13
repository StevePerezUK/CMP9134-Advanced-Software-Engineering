#!/bin/env python3

from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2,units="km"):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    if units == "km":
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles or 3444 for nautical miles - Knots.  Determines return value units.
    elif units == "kts":
        r = 3444
    elif units == "miles":
        r = 3956
    return c * r