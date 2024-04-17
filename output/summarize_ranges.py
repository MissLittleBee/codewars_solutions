"""Kata - Summarize ranges

completed at: 2024-04-16 21:02:17
by: Jakub Červinka

Given a sorted array of numbers, return the summary of its ranges.


## Examples
```javascript
summaryRanges([1, 2, 3, 4]) === ["1->4"]
summaryRanges([1, 1, 1, 1, 1]) === ["1"]
summaryRanges([0, 1, 2, 5, 6, 9]) === ["0->2", "5->6", "9"]
summaryRanges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]) === ["0->7"]
summaryRanges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]) === ["0->7", "9->10"]
summaryRanges([-2,0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]) ===["-2", "0->7", "9->10", "12"]
```
```python
summary_ranges([1, 2, 3, 4]) == ["1->4"]
summary_ranges([1, 1, 1, 1, 1]) == ["1"]
summary_ranges([0, 1, 2, 5, 6, 9]) == ["0->2", "5->6", "9"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]) == ["0->7"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]) == ["0->7", "9->10"]
summary_ranges([-2, 0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]) == ["-2", "0->7", "9->10", "12"]
```
```ruby
summary_ranges([1, 2, 3, 4]) == ["1->4"]
summary_ranges([1, 1, 1, 1, 1]) == ["1"]
summary_ranges([0, 1, 2, 5, 6, 9]) == ["0->2", "5->6", "9"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]) == ["0->7"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]) == ["0->7", "9->10"]
summary_ranges([-2, 0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]) == ["-2", "0->7", "9->10", "12"]
```
"""

from itertools import pairwise


def find_consecutive_start(arr):
    for i, (a, b) in enumerate(pairwise(arr)):
        if b > a + 1:
            return arr[:i + 1]
    return arr


def ranges_to_string(ranges):
    result = []
    for start, end in ranges:
        if start == end:
            result.append(str(start))
        else:
            result.append(f'{start}->{end}')
    return result


def summary_ranges(arr):
    # setup
    start, end = 0, 1
    output = []

    # edge cases
    if not arr: return output
    if len(arr) == 1: return [str(arr[0])]

    while arr:
        sub_arr = find_consecutive_start(arr)
        output.append([sub_arr[0], sub_arr[-1]])
        arr = arr[len(sub_arr):]

    output = ranges_to_string(output)
    return output
            
        
