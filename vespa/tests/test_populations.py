from __future__ import print_function, division

from vespa.populations import HEBPopulation
from vespa.populations import EBPopulation

import os, os.path
import tempfile
TMP = tempfile.gettempdir()

from vespa.transit_basic import MAInterpolationFunction

MAfn = MAInterpolationFunction(nzs=50,nps=100,pmin=0.05,pmax=1/0.05)

def test_heb(filename=os.path.join(TMP,'test_heb.h5')):
    mass = (0.83, 0.05)
    age = (9.6, 0.1)
    feh = (0.0, 0.1)
    mags = {'H': 10.211,
            'J': 10.523,
            'K': 10.152000000000001}
    period = 289.8622
    pop = HEBPopulation(mass=mass, age=age, feh=feh, mags=mags,
                       period=period, n=100, MAfn=MAfn)
    pop.save_hdf(filename, overwrite=True)
    pop2 = HEBPopulation().load_hdf(filename)
    os.remove(filename)


def test_eb(filename=os.path.join(TMP,'test_eb.h5')):
    mass = (0.83, 0.05)
    age = (9.6, 0.1)
    feh = (0.0, 0.1)
    mags = {'H': 10.211,
            'J': 10.523,
            'K': 10.152000000000001}
    period = 289.8622
    pop = EBPopulation(mass=mass, age=age, feh=feh, mags=mags,
                       period=period, n=100, MAfn=MAfn)

    pop.save_hdf(filename, overwrite=True)
    pop2 = EBPopulation().load_hdf(filename)
    os.remove(filename)