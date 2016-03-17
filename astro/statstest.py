"""Module to hold methods for testing out stats routines."""
# import myfun as m
# import myfun.astro as stats
import specops
import stats
import matplotlib.pyplot as plt
import numpy as np


def dotimes(times=2, tol=2):
    """Filter data greater than 2 sigma from average."""
    s = specops.rspec()
    wls = s.wls
    data = s.data
    pss, fll = stats.filter_tolerance(wls, data, tol)
    plt.xlabel("Wavelength")
    ob_name = s.obj_name
    name = s.fname
    plt.title(ob_name + '\n' + name)
    plt.plot(pss[0], pss[1], '-b', fll[0], fll[1], '-r')
    s.close()
    pss2, fll2 = stats.filter_tolerance(pss[0], pss[1], tol)
    plt.clf()
    plt.title(ob_name + '\n' + name)
    plt.plot(pss2[0], pss2[1], '.b',
             fll2[0], fll2[1], '-r',
             fll[0], fll[1], '.g')



def dotest(starfilt='', times=2, tol=2, mksize=[1, 1, 1]):
    s = specops.rspec(filt=starfilt)
    wls = s.wls
    data = s.data
    pss, fll = stats.filter_tolerance(wls, data, tol)
    plt.xlabel("Wavelength")
    ob_name = s.obj_name
    name = s.fname
    plt.title(ob_name + '\n' + name)
    plt.plot(pss[0], pss[1], '-b', fll[0], fll[1], '-r')
    s.close()
    pss2, fll2 = stats.filter_tolerance(pss[0], pss[1], tol)
    plt.clf()
    plt.title(ob_name + '\n' + name)
    plt.plot(pss2[0], pss2[1], '.b', ms=mksize[0])
    plt.plot(fll2[0], fll2[1], '.r', ms=mksize[1])
    plt.plot(fll[0], fll[1], '.g',   ms=mksize[2])

def testplot():
    xdata = [x for x in range(50)]
    ydata = [x**3 for x in range(50)]
    plt.plot(xdata, ydata)


def normalize_data(wls, data, tol=2):
    """Returns normalized data."""
    # Flag all data points greater than tol stddevs away from the average


    # pss, fll = stats.filter_tolerance(wls, data, tol)

    # Fit all unflagged data with both a linear and a quadratic fit
    linear_fit = np.poly1d(np.polyfit(wls, data, 1))
    quadratic_fit = np.poly1d(np.polyfit(wls, data, 2))

    # Plot the data passed along with the two fit lines calculated
    plt.plot(wls, data, 'o', ms=1, color='black')
    linear_plot, = plt.plot(wls, linear_fit(wls), '-b', label='linear')
    quadratic_plot, = plt.plot(wls, quadratic_fit(wls), '-r',
                               label='quadratic')
    plt.xlabel('Wavelength (Angstroms)')
    plt.ylabel('Intensity Values')
    plt.title('Data with 2 fits')
    plt.legend([linear_plot, quadratic_plot],
               ['Linear Fit', 'Quadratic Fit'],
               loc=0
               )
    # Choose best fit from R^2 value
    # Flag all data points greater than tol stddevs away from the new average
    # Fit all unflagged data same as before
    # Divie data passed by last fit, the continuum line
