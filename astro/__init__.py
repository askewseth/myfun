"""Initalizer for astro app in usefulfunctions module."""
from locations import *
from specops import *
import sys
import os
sys.path.insert(0, os.getcwd())
from stats import *
from statstest import *


loc, usr = get_location()
