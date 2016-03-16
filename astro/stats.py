"""Module to hold functions for normalizing and getting stats about specs."""
import myfun as m
import numpy as np
import matplotlib.pyplot as plt

def filter_tolerance(wls, data, tol=2, pas=False):
    sigma = np.std(data)
    avg = np.average(data)
    plotdata = zip(wls, data)
    filt1plot = filter(lambda x: abs(avg-x[1]) < tol * sigma, plotdata)
    filt1plotnot = filter(lambda x: abs(avg-x[1]) > tol * sigma, plotdata)
    fil1_wls = [x[0] for x in filt1plot]
    fil1_wlsnot = [x[0] for x in filt1plotnot]
    fil1_data = [x[1] for x in filt1plot]
    fil1_datanot = [x[1] for x in filt1plotnot]
    if pas:
        return [fil1_wls, fil1_data]
    return [fil1_wls, fil1_data], [fil1_wlsnot, fil1_datanot]


def filter_iter(wls, data, tol=2, its=2):
    fails = []
    for x in range(its):
        ps1, fl1 = filter_tolerance(wls, data, tol)
        fails.extend(fl1)
        ps2, fl2 = filter_tolerance(ps1[0], ps1[1])
        fails.extend(fl2)
        wls, data = ps2
    return wls, fails.extends(data)



def filter_twice(wls, data, tol=2):
    pss, fll = filter_tolerance(wls, data, tol)
    pss_filt, fll_filt = filter_tolerance(pss[0], pss[1], tol)
    return pss_filt, fll_filt
