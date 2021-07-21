import math
def sphdist(lat1, lon1, lat2, lon2):
    """
        Calculates the great circle distance given
        the latitudes and longitudes of two points.
        Input
            lat1, lon1: lat and long in degrees for the first point
            lat2, lon2: lat and long in degrees for the second point
        Output
            d: great circle distance
    """
    D = 3959
    phi1 = math.radians(lat1)
    lambda1 = math.radians(lon1)
    phi2 = math.radians(lat2)
    lambda2 = math.radians(lon2)
    dlambda = lambda2 - lambda1
    dphi = phi2 - phi1
    sinlat = math.sin(dphi/2.0)
    sinlong = math.sin(dlambda/2.0)
    alpha = (sinlat*sinlat) + math.cos(phi1) * math.cos(phi2) * (sinlong*sinlong)
    c = 2 * math.asin(min(1, math.sqrt(alpha)))
    d = D*c
    return d

if __name__ == "__main__":
    lat1, lon1 = 40, -83            # Columbus, OH
    lat2, lon2 = 39.91, 116.56      # Beijing
    print(sphdist(lat1, lon1, lat2, lon2))
