"""Kata - sum2total

completed at: 2025-02-06 12:34:39
by: Barbora Hůlová

Given a list of numbers, repeatedly sum adjacent pairs of numbers until only one number remains. 

## Explanation

If the list is `[1, 2, 3, 4, 5]`, the first step would be:

* `1 + 2 = 3`

* `2 + 3 = 5`

* `3 + 4 = 7`

* `4 + 5 = 9`

Take the results from the first step and repeat the process of adding adjacent pairs:

* `3 + 5 = 8`

* `5 + 7 = 12`

* `7 + 9 = 16`

Continue this process until only one number remains:

* `8 + 12 = 20`

* `12 + 16 = 28`

Finally, 

* `20 + 28 = 48`

The final result for the list `[1, 2, 3, 4, 5]` is `48`.

## Examples

* For the list `[-1, -1, -1]`, the result is `-4`.

* For the list `[1, 2, 3, 4]`, the result is `20`.

## Note

* The input list will always contain at least one number.

* All elements in the list will be valid numbers.
"""

def total(arr):
    while len(arr) > 1:
        new_arr = []
        for i in range(len(arr) - 1):
            sum_value = arr[i] + arr[i + 1]
            new_arr.append(sum_value)
        arr = new_arr
    return arr[0]
