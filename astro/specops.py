"""File holding useful functions for spectra."""
import os
import sys
import random as rand
import locations as loc
sys.path.insert(0, '/home/' + loc.get_location()[1] + '/AstroML/')
from Spectrum import spectrum
import myfun as m

# user = loc.get_location[1]

def rspec(path=None, local=False):
    """Randomly choose one fits file to make spectrum from and return."""
    user = loc.get_location()[1]
    if path is None:
        if user == 'extra':
            os.chdir('/home/extra/Desktop/AllHAraw/fits/')
            path = '/home/extra/Desktop/AllHAraw/fits/'
        elif user == 'oort':
            path = '/home/oort/Downloads/AllHA/'
        else:
            print 'ERROR RETURNING NONE'
            return None
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


def rspecs(num=1, path=None, local=False):
    """Allow for getting a list of multiple specs."""
    if path is None:
        try:
            os.chdir('/home/extra/Desktop/AllHAraw/fits/')
            path = '/home/extra/Desktop/AllHAraw/fits/'
        except:
            path = '/home/oort/Downloads/AllHA/'
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


def plot_rspecs(num=1, ret=False, path=None, local=True):
    """Plot the HA ord of <num> spectra."""
    if path is None:
        try:
            os.chdir('/home/extra/Desktop/AllHAraw/fits/')
            path = '/home/extra/Desktop/AllHAraw/fits/'
        except:
            path = '/home/oort/Downloads/AllHA/'
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
    if path is None:
        try:
            os.chdir('/home/extra/Desktop/AllHAraw/fits/')
            path = '/home/extra/Desktop/AllHAraw/fits/'
        except:
            path = '/home/oort/Downloads/AllHA/'
    files = m.ls(True, path=path, filt='.fits')
    len_files = len(files)
    print 'There are {} files to be processed'.format(len_files)
    specs = {}
    print 'FULL INFO'
    for i, x in enumerate(files):
        print '\rFile Number: {0}  \tPercentage Done: {1:.6}'\
                    .format(i, float(i) / len_files * 100),
        try:
            s = spectrum(x)   # make the spectrum object
            # go through and write all the info about it in dic
            infodic = {}
            infodic['date'] = s.date
            infodic['fname'] = s.fname
            infodic['HA'] = s.HA
            infodic['head'] = s.head.copy()
            infodic['hjd'] = s.hjd
            infodic['obj_name'] = s.obj_name
            infodic['path'] = s.path
            infodic['vhel'] = s.vhel
            infodic['wls'] = s.wls
            specs[s.fname] = infodic
            s.close()         # make sure to close file
        except Exception as e:
            print 'error', e
    return specs
