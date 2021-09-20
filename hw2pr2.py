# CS5 Gold, hw2pr2
# Filename: hw2pr2.py
# Name: Leah Hall and antonia hekster 
# Problem description: Sleepwalking student
import sys
sys.setrecursionlimit(50000)
import random
import time
import sys
def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])
def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)
def rwsteps(start, low, high):
    """ rwsteps models a random walker that
        * starts at the int argument, start  
        * goes UNTIL reaching low or high
          (low will always be less than high)

        rwsteps returns the number of steps the
        walker needed to reach the lower or upper bound
    """
    print("low, high, start are", low, high, start)   # show all of the arguments, as numbers...
    print("_"*(start-low) + 'S')     # this is the beginning of a "terminal-graphics" wandering...
    time.sleep(0.05)

    if start <= low or start >= high:
        print '|' + (start - low) * ' ' + 'T.T' + (hi - start) * ' ' + '|'
        return 0

    else:
        newpos = start + rs()   # take one step, from start to newpos!
        print '|' + (start - low) * ' ' + 'T.T' + (hi - start) * ' ' + '|'
        return 1 + rwsteps(newpos, low, high)

