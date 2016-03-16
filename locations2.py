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
