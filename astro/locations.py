"""File containing useful functions for switching b/t computers."""
import os

def get_location():
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
