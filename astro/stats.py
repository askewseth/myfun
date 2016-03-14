"""Module to hold functions for normalizing and getting stats about specs."""
import myfun as m
import numpy as np

def filter_tolerance(wls, data, tol=2):
    sigma = np.std(data)
    avg = np.average(data)
    plotdata = zip(wls, data)
    filt1plot = filter(lambda x: abs(avg-x[1]) <= tol * sigma, plotdata)
    filt1plotnot = filter(lambda x: abs(avg-x[1]) > tol * sigma, plotdata)
    fil1_wls = [x[0] for x in filt1plot]
    fil1_wlsnot = [x[0] for x in filt1plotnot]
    fil1_data = [x[1] for x in filt1plot]
    fil1_datanot = [x[1] for x in filt1plotnot]
    return [fil1_wls, fil1_data], [fil1_wlsnot, fil1_datanot]
