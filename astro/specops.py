"""File holding useful functions for spectra."""
import os
import sys
import random as rand
import locations as loc
sys.path.insert(0, '/home/' + loc.get_location()[1] + '/AstroML/')
from Spectrum import spectrum


def rspec(path='/home/extra/Desktop/AllHAraw/fits/', local=False):
    if local:
        path = '/home/extra/AstroFiles/fits/'
    fits = [x for x in os.listdir(path) if '.fits' in x]
    fname = path + rand.choice(fits)
    try:
        s = spectrum(fname)
        return s
    except:
        fname = path + rand.choice(fits)
        try:
            s = spectrum(fname)
            return s
        except:
            print "ERROR MAKING SPECTRUM"
            return None

    print len(fits)
    return path


def rspecs(num=1, path='/home/extra/Desktop/AllHAraw/fits/', local=False):
    """Allow for getting a list of multiple specs."""
    if local:
        path = '/home/extra/AstroFiles/fits/'
    fits = [x for x in os.listdir(path) if '.fits' in x]
    fnames = [path + rand.choice(fits) for f in fits]
    rand.shuffle(fnames)
    specs = []
    counter = 0
    while len(specs) < num:
        try:
            s = spectrum(fnames[counter])
            specs.append(s)
        except:
            pass
        counter += 1
        if  counter > len(fnames):
            break
    return specs


def plot_rspecs(num=1, ret=False, path='/home/extra/Desktop/AllHAraw/fits/', local=True):
    """Plot the HA ord of <num> spectra."""
    specs = rspecs(num, path, local)
    bad = []
    for i, s in enumerate(specs):
        try:
            s.plotHA()
        except Exception as e:
            bad.append([i, e, s.path])
    print '\nBAD FILES: (', len(bad), ')'
    for x, y, z in bad:
        print '\n\t{0}:  {1}\n\t\tDate: {2}'.format(x, y, z)
    if ret:
        return specs
    return
