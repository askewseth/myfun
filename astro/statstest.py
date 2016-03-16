"""Module to hold methods for testing out stats routines."""
import myfun as m
import matplotlib.pyplot as plt

def dotimes(times=2, tol=2):
    s = m.rspec()
    wls = s.wls
    data = s.data
    pss, fll = m.filter_tolerance(wls, data, tol)
    plt.xlabel("Wavelength")
    ob_name = s.obj_name
    name = s.fname
    plt.title(ob_name + '\n' + name)
    plt.plot(pss[0], pss[1], '-b', fll[0], fll[1], '-r')
    s.close()
    pss2, fll2 = m.filter_tolerance(pss[0], pss[1], tol)
    plt.clf()
    plt.title(ob_name + '\n' + name)
    plt.plot(pss2[0], pss2[1], '.b', fll2[0], fll2[1], '-r', fll[0], fll[1], '.g')



def dotest(starfilt='', times=2, tol=2, mksize=[1, 1, 1]):
    s = m.rspec(filt=starfilt)
    wls = s.wls
    data = s.data
    pss, fll = m.filter_tolerance(wls, data, tol)
    plt.xlabel("Wavelength")
    ob_name = s.obj_name
    name = s.fname
    plt.title(ob_name + '\n' + name)
    plt.plot(pss[0], pss[1], '-b', fll[0], fll[1], '-r')
    s.close()
    pss2, fll2 = m.filter_tolerance(pss[0], pss[1], tol)
    plt.clf()
    plt.title(ob_name + '\n' + name)
    plt.plot(pss2[0], pss2[1], '.b', ms=mksize[0])
    plt.plot(fll2[0], fll2[1], '.r', ms=mksize[1])
    plt.plot(fll[0], fll[1], '.g',   ms=mksize[2])

def testplot():
    xdata = [x for x in range(50)]
    ydata = [x**3 for x in range(50)]
    plt.plot(xdata, ydata)
