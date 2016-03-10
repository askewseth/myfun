"""Houses and holds methods for directory of methods."""

astro_mods = {
    'locations': ['get_location()'],
    'specops': [
        "rspec(path='/home/extra/Desktop/AllHAraw/fits/', local=False)",
        "rspecs(num=1, path='/home/extra/Desktop/AllHAraw/fits/', \
                    local=False)",
        "plot_rspecs(num=1, ret=False, \
                path='/home/extra/Desktop/AllHAraw/fits/', local=True)"
        ]
}

mods = {
    'usefun': [
        "pwd(show=False)",
        "ls(show=True, dirs=None, filt='')",
        "rmpyc(ask=True, path=None)"
        ],
    'printers': ["cmp_funs()", "make_importable()"],
    'specstuff': [],
    'dir': ['dir()']
}

def dir():
    print len(astro_mods)
    print len(mods)
