"""Some functions I tend to use a lot when programming."""
import os


def pwd(show=False):
    """Print the current path."""
    d = ''.join([os.getcwd(), '/'])
    if show:
        print d
        return None
    return d


def ls(show=True, dirs=None, filt=''):
    """
    Get the files and directories in the current working dir.

    Params:
        returns:
            -if False print's results and return's None
            -if True returns results as list full paths
                --DEFAULT: False
        dirs:
            -if True only get's directories
            -if False get's everything but directories
            -if None get's everything
                --DEFAULT: None
        filter:
            -String- only shows results containing that string
                --DEFAULT: ''

    If called as:
        m.ls(False)
    interpreted as:
        m.ls(show=False)

    """
    bpath = ''.join([os.getcwd(), '/'])
    if dirs is not None:
        if dirs:
            # 2nd el (list of dirs) of 1st el (tuple of dir info)
            # returned in a generator
            d_raw = os.walk(os.getcwd()).next()[1]
        else:
            d_raw = os.walk(os.getcwd()).next()[2]
    else:
        d_raw = os.listdir(os.getcwd())
    d_nodots = filter(lambda x: x[0] != '.', d_raw)  # remove hidden dirs
    d_filtered = [x for x in d_nodots if filt in x]    # filter if given
    d_nopath = sorted(d_filtered)  # final values of d w/o path, to show
    d_path = [bpath + x for x in d_nopath]
    if show:
        for i, x in enumerate(d_nopath):
            print i, x
        return None
    return d_path


def cd(path, full=False):
    """Replicates regular cd, if '/' not first char path is relative."""
    if path[0] != '/' or full:
        os.chdir(path)
        return
    elif path == '..':
        cur_path = pwd().split('/')
        os.chdir('/'.join(cur_path[:-1]))
    else:
        bpath = os.getcwd() + '/'
        os.chdir(bpath + path)
        return

def rmpyc(ask=True, path=None):
    """Remove all .pyc files in path, path defaults to cwd."""
    if path is None:
        path = pwd()
    pycfiles = [x for x in os.listdir(path) if x.split('.')[-1] == 'pyc']
    if len(pycfiles) == 0:
        print '\nNo .pyc files were found'
        return
    # Show .pyc files in directory
    print '\n.PYC FILES IN ', path, ':'
    for i, x in enumerate(pycfiles):
        print '\t', i, x
    # Make sure they want to delete the files if ask is true
    if ask:
        ans = raw_input("Are you sure you want to delete these files? ([Y]/n): ")
        if 'n' in ans.lower():
            print 'Did not delete files'
            return
    # Delete files in pycfiles
    for f in pycfiles:
        os.remove(f)
        print 'removed ', f
    return
