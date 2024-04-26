"""Kata - Element  equals its index

completed at: 2024-04-25 19:08:20
by: Jakub Červinka

```if:python
Given a sorted array of distinct integers, write a function `index_equals_value` that returns the lowest index for which `array[index] == index`.  
Return `-1` if there is no such index.
```
```if:haskell,javascript
Given a sorted array of distinct integers, write a function `indexEqualsValue` that returns the lowest index for which `array[index] == index`.  
Return `-1` if there is no such index.
```
```if:rust
Given a sorted slice of distinct integers, write a function `index_equals_value` that returns the lowest index for which `slice[index] == index`.  
Return `-1` if there is no such index.
```

Your algorithm should be very performant.

[input] array of integers ( with `0`-based nonnegative indexing )  
[output] integer

### Examples:

<!-- no need to add more languages really. but leave "python" in or words get coloured -->
```python
input: [-8,0,2,5]
output: 2 # since array[2] == 2

input: [-1,0,3,6]
output: -1 # since no index in array satisfies array[index] == index
```
### Random Tests Constraints:

```if:python,javascript
Array length: 200 000
```
```if:rust
Slice length: 200 000
```
```if:haskell
Array length: 10 000
```

Amount of tests: 1 000

```if:python
Time limit: 1.5 s
```
```if:haskell,javascript,rust
Time limit: 150 ms
```
___

If you liked this Kata check out my more complex creations:

Find the neighbourhood in big dimensions. [Neighbourhood collection](https://www.codewars.com/collections/5b2f4db591c746349d0000ce)

The [Rubik's cube](https://www.codewars.com/kata/5b3bec086be5d8893000002e)
"""

def index_equals_value(arr):
    left, right = 0, len(arr) - 1
    smallest_match = float('inf')

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == mid:
            smallest_match = min(smallest_match, mid)
            right = mid - 1
        elif arr[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1

    return smallest_match if smallest_match != float('inf') else -1
