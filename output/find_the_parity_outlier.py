"""Kata - Find The Parity Outlier

completed at: 2024-04-12 13:34:19
by: Barbora Hůlová

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer `N`. Write a method that takes the array as an argument and returns this "outlier" `N`.

## Examples

```
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
```

"""

def find_outlier(integers):
    odd = []
    even = []
    
    for i in integers:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(odd) > 1:
        return even[0]
    else:
        return odd[0]
    
