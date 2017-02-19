# -*- coding: utf-8 -*-
"""Finds the most valuable items to put into a knapsack."""

FILENAME = "test-data-2.csv"
TOTE_LENGTH = 45
TOTE_WIDTH = 30
TOTE_HEIGHT = 35
TOTE_VOLUME = TOTE_LENGTH * TOTE_WIDTH * TOTE_HEIGHT

PRODUCTS = []

def check_dimension(vol):
    """Checks that the item fits in the tote."""
    if vol > TOTE_VOLUME:
        return False
    else:
        return True

def pick(products, capacity):
    """Decides which products to pick."""
    sortedproducts = sorted(products, key=lambda product: product['volume'])
    j = capacity
    result = []
    for i in xrange(len(sortedproducts), 0, -1):
        if bestvalue(i, j) != bestvalue(i - 1, j):
            result.append(products[i - 1])
            j -= products[i - 1]['volume']
    result.reverse()
    return result

def bestvalue(index, maxvol):
    """Returns the total price of the most valuable subsequence of the first
    i elements in products whose volume sum to no more than tote volume."""
    if index == 0:
        return 0
    value = PRODUCTS[index-1]['price']
    itemvolume = PRODUCTS[index-1]['volume']
    if itemvolume > maxvol:
        return bestvalue(index - 1, maxvol)
    else:
        return max(bestvalue(index - 1, maxvol - itemvolume) + value, # case that this item is taken
                   bestvalue(index - 1, maxvol)) # case that this item is not taken

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
