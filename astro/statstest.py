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


def normalize_spec(wls, data, tol=2):
    passed_wls, passed_data = np.array(wls), np.array(data)
    """Returns normalized data."""
    # Flag all data points greater than tol stddevs away from the average
    pss, fll = stats.filter_tolerance(wls, data, tol)
    wls, data = pss[0], pss[1]
    # Fit all unflagged data with both a linear and a quadratic fit
    linear_fit = np.poly1d(np.polyfit(wls, data, 1))
    quadratic_fit = np.poly1d(np.polyfit(wls, data, 2))

    # Plot the data passed along with the two fit lines calculated
    plt.plot(wls, data, 'o', ms=1, color='black')
    plt.plot(fll[0], fll[1], '.r', ms=3)
    linear_plot, = plt.plot(wls, linear_fit(wls), '-b', label='linear')
    quadratic_plot, = plt.plot(wls, quadratic_fit(wls), '-r',
                               label='quadratic')
    plt.xlabel('Wavelength (Angstroms)')
    plt.ylabel('Intensity Values')
    plt.title('First filter, from average')
    plt.legend([linear_plot, quadratic_plot],
               ['Linear Fit', 'Quadratic Fit'],
               loc=0
               )
    plt.show()
    # Choose best fit from R^2 value
    def calc_r_squared(fit, wls, data):
        # R^2 = 1 - SSline/SStotal
        wls, data = map(np.array, [wls, data])
        ss_line_data = data - fit(data)
        ss_line = sum([x**2 for x in ss_line_data])
        avg = np.average(data)
        ss_tot = sum([(wl - avg)**2 for wl in wls])
        r_squared = 1-(ss_line/ss_tot)
        return r_squared
    r2_linear = calc_r_squared(linear_fit, wls, data)
    r2_quadratic = calc_r_squared(quadratic_fit, wls, data)
    print "R^2 Values:"
    print '\tLinear: {}'.format(r2_linear)
    print '\tQuadratic: {}'.format(r2_quadratic)

    # Flag all data points greater than tol stddevs away from the new average
    print 'assuming linear fit better'
    new_pss, new_fll = stats.filter_tolerance_fit(wls, data,
                                                  linear_fit, tol=tol)
    wls, data = new_pss[0], new_pss[1]
    plt.plot(wls, data, 'o', ms=1, color='black')
    plt.plot(new_fll[0], new_fll[1], '.g', ms=2)
    plt.plot(fll[0], fll[1], '.r', ms=3)
    plt.title('Second filter, from first fit line')
    plt.show()

    # Fit all unflagged data same as before
    linear_fit = np.poly1d(np.polyfit(wls, data, 1))
    quadratic_fit = np.poly1d(np.polyfit(wls, data, 2))
    plt.plot(wls, data, 'o', ms=1, color='black')
    plt.plot(new_fll[0], new_fll[1], '.g', ms=2)
    plt.plot(fll[0], fll[1], '.r', ms=3)
    linear_plot, = plt.plot(wls, linear_fit(wls), '-b', label='linear')
    quadratic_plot, = plt.plot(wls, quadratic_fit(wls), '-r',
                               label='quadratic')
    plt.xlabel('Wavelength (Angstroms)')
    plt.ylabel('Intensity Values')
    plt.title('Newly fit second data')
    plt.legend([linear_plot, quadratic_plot],
               ['Linear Fit', 'Quadratic Fit'],
               loc=0
               )
    plt.show()

    r2_linear2 = calc_r_squared(linear_fit, wls, data)
    r2_quadratic2 = calc_r_squared(quadratic_fit, wls, data)
    print "R^2 Values:"
    print '\tLinear: {}'.format(r2_linear2)
    print '\tQuadratic: {}'.format(r2_quadratic2)

    # Divie data passed by last fit, the continuum line
    normal_data = passed_data/linear_fit(passed_wls)
    print 'normal length', len(normal_data)
    plt.plot(passed_wls, normal_data, '.', color='orange')
    # return (r2_linear, r2_quadratic)
