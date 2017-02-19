# -*- coding: utf-8 -*-
"""Finds the most valuable items to put into a knapsack."""

import functools

FILENAME = "test-data-2.csv"
TOTE_LENGTH = 45
TOTE_WIDTH = 30
TOTE_HEIGHT = 35
TOTE_VOLUME = TOTE_LENGTH * TOTE_WIDTH * TOTE_HEIGHT

PRODUCTS = []

class Memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).'''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
           # uncachable -- for instance, passing a list as an argument.
           # Better to not cache than to blow up entirely.
            return self.func(*args)
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

def check_dimension(vol):
    """Checks that the item fits in the tote."""
    if vol > TOTE_VOLUME:
        return False
    else:
        return True

@Memoized
def bestvalue(index, maxvol):
    """Returns the total price of the most valuable subsequence of the first
    i elements in products whose volume sum to no more than tote volume."""
    if index == 0:
        return 0
    value = PRODUCTS[index - 1]['price']
    itemvolume = PRODUCTS[index - 1]['volume']
    if itemvolume > maxvol:
        return bestvalue(index - 1, maxvol)
    else:
        return max(bestvalue(index - 1, maxvol - itemvolume) + value, # case that this item is taken
                   bestvalue(index - 1, maxvol)) # case that this item is not taken

def pick(products, capacity):
    """Decides which products to pick."""
    j = capacity
    result = []
    for i in xrange(len(products), 0, -1):
        if bestvalue(i, j) != bestvalue(i - 1, j):
            result.append(products[i - 1])
            j -= products[i - 1]['volume']
    result.reverse()
    return result

with open(FILENAME, "rb") as f:
    for line in f:
        data = [int(e) for e in line.strip().split(",")]
        volume = data[2] * data[3] * data[4]
        item = {'id': data[0],
                'price': data[1],
                'length': data[2],
                'width': data[3],
                'height': data[4],
                'weight': data[5],
                'volume': volume}
        if check_dimension(item['volume']):
            PRODUCTS.append(item)

# Print the sum of the product ids
print sum([item['id'] for item in pick(PRODUCTS, TOTE_VOLUME)])
