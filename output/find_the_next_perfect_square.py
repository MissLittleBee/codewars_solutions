"""Kata - Find the next perfect square!

completed at: 2023-06-01 06:46:53
by: Jakub Červinka

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the `findNextSquare` method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.  

If the parameter is itself not a perfect square then `-1` should be returned. You may assume the parameter is non-negative.

**Examples:(Input --> Output)**

```
121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square
```

"""

from itertools import count

def find_next_square(sq):
    if not (sq ** 0.5).is_integer():
        return -1
    for num in count(start=sq + 1):
        if (num ** 0.5).is_integer():
            return num
    
