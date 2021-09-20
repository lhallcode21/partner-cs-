# CS5 Gold, hw2pr2
# Filename: hw2pr2.py
# Name: Leah Hall and Antonia Hekster 
# Problem description: Sleepwalking student

import sys
sys.setrecursionlimit(50000)
import random  

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])

import random
random.choice([-1, 1])

import time

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

import time

def rwsteps(start, low, high):
    """ rwsteps models a random walker that
        * starts at the int argument, start  
        * goes UNTIL reaching low or high
          (low will always be less than high)

        rwsteps returns the number of steps the
        walker needed to reach the lower or upper bound
    """
    print('|' + "_"*(start-low) + 'S' + "_"*(high-start)+ '|')
    time.sleep(0.05)

    if start <= low or start >= high:
        return 0

    else:
        newpos = start + rs()   # take one step, from start to newpos!
        print('|' + '_'*(newpos-low) + 'S' + '_'*(high-newpos) + '|')
        return 1 + rwsteps(newpos, low, high)
