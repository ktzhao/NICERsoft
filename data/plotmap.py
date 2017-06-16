#!/usr/bin/env python
from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt

import astropy.units as u
from astropy.time import Time

from mpl_toolkits.basemap import Basemap

from nicer.mcc import MCC

saa_lon, saa_lat = np.loadtxt('saa_lonlat.txt',unpack=True)

MET0 = Time("2014-01-01T00:00:00.0",scale='utc')
GPS0 = Time("1980-01-06T00:00:00",scale='utc')

gpssec, overshootrate = np.loadtxt('data/20170614_turnon_all_particles.lc',
    unpack=True,dtype=np.float)

eph = MCC('data/MCC1_On_Console_20171631440_V01.txt')
t = gpssec*u.s + GPS0
met = (t-MET0).to(u.s).value

lat, lon = eph.latlon(met)

map = Basemap(projection='cyl', resolution = 'l',
              lat_0=0, lon_0=0)
map.drawcoastlines()
map.scatter(lon, lat,c=overshootrate,cmap='jet')
map.plot(saa_lon,saa_lat,'g',lw=2)
plt.show()
