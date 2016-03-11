colors = {
        'PURPLE': '\033[95m',
        'CYAN': '\033[96m',
        'DARKCYAN': '\033[36m',
        'BLUE': '\033[94m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'RED': '\033[91m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
        'END': '\033[0m'
}
shortcuts = {
        'p': 'PURPLE',
        'c': 'CYAN',
        'dc': 'DARKCYAN',
        'bl': 'BLUE',
        'g': 'GREEN',
        'y': 'YELLOW',
        'r': 'RED',
        'b': 'BOLD',
        'ul': 'UNDERLINE',
        'e': 'END'
}

def bold(string, action='b'):
    "Initalize color object."
    action = action.replace(" ", "")
    # make sure action valid
    passed = False
    # shortcut was given
    if len(action) < 3:
        if action.lower() in shortcuts.keys():
            passed = True
    else:
        if action.upper() in shortcuts.values():
            passed = True
    if not passed:
        print 'INVALID ACTION'
        return string
    # get the value for the action
    if len(action) < 3:
        color_name = shortcuts[action.lower()]
        color_val = colors[color_name]
    else:
        color_val = colors[action.upper()]
    end_val = colors['END']
    # apply action to string
    newstring = color_val + string + end_val
    # print 'from prog: ', newstring
    return color_val + string + end_val
