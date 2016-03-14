"""File containing useful functions for switching b/t computers."""
import os


def get_location():
    """Figure out which computer is currently being used, return loc, usr."""
    loc = 'UNKNOWN'
    usr = 'UNKNOWN'
    try:
        os.chdir('/home/extra/')
        return 'apt', 'extra'
    except:
        try:
            os.chdir('/home/oort/')
            return 'school', 'oort'
        except:
            try:
                os.chdir('/home/seth/')
                return 'apt', 'seth'
            except:
                pass
    return loc, usr

# Define location and user for use in other methods
loc, usr = get_location()

path_shortcuts = {
    ('All', 'AllBess', 'AllHA', 'AllHAraw', 'BeSS'): {
        'oort': '/home/oort/AllHA/',
        'extra': '/home/extra/Desktop/AllHAraw/fits/',
        'seth': '/home/seth/AllHA/'
         },
    ('Loc', 'Local', 'LocalFiles', 'AstroFiles'): {
        'oort': '/home/oort/AstroFiles/',
        'extra': '/home/extra/AstroFiles/',
        'seth': '/home/seth/AstroFiles/'
    },
    ('myfun', ): {
        'oort': '/home/oort/myfun/',
        'extra': '/home/extra/myfun/',
        'seth': '/home/seth/myfun/'
    }
}


def shortpath(shortcut=None):
    """Return full path for given shortcut name."""
    keys = path_shortcuts.keys()
    if shortcut is None:
        for tup in keys:
            print '\t'.join(tup)
        return None
    short = ''.join(map(lambda x: x.lower(), shortcut.split()))
    for tup in keys:
        lowertup = map(lambda x: x.lower(), tup)
        if short in lowertup:
            return path_shortcuts[tup][usr]
    print 'Shortcut not found.  Available shortcuts: '
    for tup in keys:
        print '\t'.join(tup)
    return None
