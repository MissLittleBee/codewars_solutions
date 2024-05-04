"""Kata - Find the crossing ( graphic calculations )

completed at: 2024-05-03 13:34:17
by: Jakub Červinka

## Description
You are given four tuples. In each tuple there is coordinates x and y of a point. There is one and only one line, that goes through two points, so with four points you can have two lines: first and second tuple is two points of a first line, thirs and fourth tuple is two points of the second line. Your task is to find and return a tuple with x and y coordinates of lines crossing point.

Numbers can be positive as well as negative, integer or floats. Your answer shouldn't be rounded!!

Note, that if two lines are the same ( have infinite crossing points ) or parallel ( have no crossing points ), you will need to return ```None```.

![Example on graphic](https://justpaste.it/img/a6760541d86f232527c516f6882c28dc.png "Example on graphic")

## Examples
``` python
find_the_crossing((5,3), (10,4), (5,7.5), (10,7)) => (20, 6) #from the graphic above
find_the_crossing((5,3), (10,4), (20,6), (0,2)) => -1 #edge case for two identical lines
find_the_crossing((5,3), (10,4), (5,5), (10,6)) => -1 #edge case for two parallel lines 
```
## Tests
There will be example tests, random tests and tests on big numbers.

**Example tests** are pre programmed tests for debugging.

**Random tests** are generated randomly, where ```-1000 ≤ x ≤ 1100```. There is still will some with parallel and identical lines.

**Tests on big numbers** are random tests where ```-1000000000 ≤ x ≤ 1000000000```
"""

import numpy as np

def find_the_crossing(a, b, c, d):
    s = np.vstack([a, b, c, d])         # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return None
    return (x/z, y/z)
