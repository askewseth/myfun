"""Initalizer for my commonly used functions."""
import os
path = os.getcwd() + '/'
from usefun import *
from printers import *
# from dirs import *
from colorfun import *
from picklefun import *
from locations2 import *
from oneliners import *
import sys
sys.path.insert(0, path + 'astro/')
# import astro


# restore original path
os.chdir(path)

pi = 3.14
