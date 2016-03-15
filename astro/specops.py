"""File holding useful functions for spectra."""
import os
import sys
import random as rand
import locations as loc
import myfun as m
sys.path.insert(0, '/home/' + loc.get_location()[1] + '/AstroML/')
from Spectrum import spectrum


def rspec(path=None, local=False, filt=""):
    """Return a random spectra built from fits file in given path."""
    # Get path
    if path is None:
        path = m.shortpath('All')
    if local:
        path = '/home/extra/AstroFiles/fits/'
    fits = [x for x in os.listdir(path) if '.fits' in x]
    fits = [x for x in fits if filt in x.lower()]
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


def rspecs(num=1, path=None, local=False, filt=''):
    """Allow for getting a list of multiple specs."""
    # Get path
    if path is None:
        path = m.shortpath('All')
        print 'got new path'
    if local:
        path = m.shortpath('local')
    fits = [x for x in m.ls(True, path=path) if '.fits' in x]
    assert len(fits) != 0, "There were no fit's files in the path"
    fits = [x for x in fits if filt in x]
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
        if counter > len(fnames):
            break
    return specs


def plot_rspecs(num=1, ret=False, path=None,
                local=True):
    """Plot the HA ord of <num> spectra."""
    # Get path
    if path is None:
        path = m.shortpath('All')
        print 'got new path'
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


def all_specs(path=None):
    """Return all of the files in the path given as spectra."""
    # Get path
    if path is None:
        path = m.shortpath('All')
        print 'got new path'
    specs = []
    m.cd(path)
    m.pwd()
    print path
    files = m.ls(True, filt='.fits')
    ercounter = 0
    print 'There are {} files'.format(len(files))
    for f in files:
        try:
            s = spectrum(f)
            specs.append(s)
            s.close()
        except:
            ercounter += 1
    print 'There were {0} errors'.format(ercounter)
    return specs


def all_objs(count=False, path=None):
    """Return all spectra as well as the number of occs for each spectra."""
    # Get path
    if path is None:
        path = m.shortpath('All')
        print 'got new path'
    specs = {}
    specnum = {}
    m.cd(path)
    m.pwd()
    print path
    files = m.ls(True, filt='.fits')
    ercounter = 0
    len_files = len(files)
    print 'There are {} files'.format(len_files)
    for i, f in enumerate(files):
        print '\rFilenumber: {0}   \tPercentage Done: {1}'\
                .format(i, float(i) / len_files),
        try:
            s = spectrum(f)
            if count:
                num = specnum.get(s.obj_name, 0)
                num += 1
                specnum[s.obj_name] = num
            else:
                specs[s.fname] = s.obj_name
            s.close()
        except:
            ercounter += 1
    print 'There were {0} errors'.format(ercounter)
    if count:
        return specs, specnum
    return specs


def all_objs_info(path=None):
    """Return all spectra as well as the number of occs for each spectra."""
    # Get path
    if path is None:
        path = m.shortpath('All')
        print 'got new path'
    specs = {}
    m.cd(path)
    m.pwd()
    print path
    files = m.ls(True, filt='.fits')
    ercounter = 0
    len_files = len(files)
    print 'There are {} files'.format(len_files)
    for i, f in enumerate(files):
        print '\rFilenumber: {0} \tPercentage Done: {1} \tNum Errors: {2}'\
                .format(i, float(i) / len_files * 100, ercounter),
        try:
            s = spectrum(f)
            specs[s.fname] = s.obj_name
            s.close()
        except:
            ercounter += 1
    print 'There were {0} errors'.format(ercounter)
    return specs
