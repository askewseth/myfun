"""File containing common pickle functions."""
import pickle as p

# add dic
def psave(obj, filename):
    if '.' not in filename:
        filename += '.p'
    with open(filename, 'wb') as handle:
        p.dump(obj, handle)
    return None

# add dic
def pload(filename):
    if '.' not in filename:
        filename += '.p'
    with open(filename, 'rb') as handle:
        ret = p.load(handle)
    return ret
