"""Houses and holds methods for directory of methods."""
import myfun as m
import astro as ast
import os

# print 'from dirs: ', ast.usr

astro_mods = {
    'locations': ['get_location()'],
    'specops': [
        "rspec(path='/home/extra/Desktop/AllHAraw/fits/', local=False)",
        "rspecs(num=1, path='/home/extra/Desktop/AllHAraw/fits/',local=False)",
        "plot_rspecs(num=1, ret=False, path='/home/extra/Desktop/AllHAraw/fits/', local=True)"
        ]
}

mods = {
    'usefun': [
        "pwd(show=False)",
        "ls(show=True, dirs=None, filt='')",
        "rmpyc(ask=True, path=None)"
        ],
    'printers': ["cmp_funs()", "make_importable()"],
    'dir': ['dir()'],
    'colorfun': ['color(action, string)']
}

def dir(args=False, fil=None, pack_name='m.'):
    """
    Print the directory of methods by the module they come from.

    Parameters:
        -fil: String, if function names contain str they're returned
            --DEFAULT: None
        -pack_name: String, is included as precursor to allow copy/paste
            --DEFAULT: 'm.'
    """
    def spacer(x):
        space = ' ' * x
        return ''.join(['\t', space, '+ '])
    space_length = 3
    if fil is not None:
        filtered = []
        for modulevar, lbl in [[mods, 'myfun base module'], [astro_mods, 'astro module']]:
            for module, methods in modulevar.iteritems():
                for method in methods:
                    color = 'c'
                    if not args:
                        mtd = method.split('(')[0] + '()'
                    else:
                        mtd = method
                    if fil in mtd:
                        filtered.append([mtd, module, lbl])
        for item in filtered:
            print ''.join(['\n',spacer(0 * space_length), m.bold(item[2].upper(), 'ul')])
            print spacer(1 * space_length), item[1]
            print ''.join([spacer(2 * space_length), m.bold(pack_name, color), m.bold(item[0], color)])
    else:
        for modulevar, lbl in [[mods, 'myfun base module'], [astro_mods, 'astro module']]:
            print ''.join(['\n',spacer(0 * space_length), m.bold(lbl.upper(), 'ul')])
            for module, methods in modulevar.iteritems():
                print spacer(1 * space_length), module
                for method in methods:
                    color = 'c'
                    if not args:
                        mtd = method.split('(')[0] + '()'
                    else:
                        mtd = method
                    print ''.join([spacer(2 * space_length), m.bold(pack_name, color), m.bold(mtd, color)])
    return



def build_dir(code=False, path=None):
    # keep original path
    orig_path = m.pwd()
    dir_path = '/home/' + ast.usr + '/myfun/'
    os.chdir(dir_path)
    # restore original path
    m.cd(orig_path, full=True)
    # remove .pyc files first
    m.rmpyc(ask=False)
    # m.pwd()
    py_files = [x for x in m.ls(False) if '.py' in x]
    if len(py_files) == 0:
        return None
    dir_lines = {}
    for fits in py_files:
        dir_lines[fits] = count(fits)
    if code:
        code_lines = []
        for moddir, vals in dir_lines.iteritems():
            for k, v in vals.iteritems():
                for line in v:
                    if line.startswith('def '):
                        code_lines.append(line)
        return code_lines
    return dir_lines

def count(fname):
    lines = {'blank': [], 'comments': [], 'code': []}
    with open(fname, 'r') as f:
        for line_raw in f:
            line = line_raw.strip()
            if line == '':
                lines['blank'].append(line)
            elif line[0] == '#':
                lines['comments'].append(line)
            else:
                lines['code'].append(line)
    return lines
