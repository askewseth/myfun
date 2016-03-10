def cmp_funs():
    """Time and show statistics between two functions."""
    print """
    # Enter function name's here:
    fun1 =
    fun2 =
    import hotshot
    import hotshot.stats
    prof = hotshot.Profile('hotshot.prof')
    prof.runcall(fun1)
    prof.runcall(fun2)
    prof.close()
    stats = hotshot.stats.load('hotshot.prof')
    stats.sort_stats('time', 'calls')
    stats.print_stats(20)
    """
    return None


def make_importable():
    """
    Print code to make python module importable.

    Prints the code to be typed into the terminal
    that adds some python module to the regularly
    importable modules in python.
    """
    print """export PYTHONPATH="$PYTHONPATH:/path_to_myapp/myapp/myapp/" """
    return None
