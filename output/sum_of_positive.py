"""Kata - Sum of positive

completed at: 2024-02-04 19:57:10
by: Jakub Červinka

You get an array of numbers, return the sum of all of the positives ones.

Example `[1,-4,7,12]` => `1 + 7 + 12 = 20`

Note: if there is nothing to sum, the sum is default to `0`.

"""

def positive_sum(arr):
    nums = []
    for num in arr:
        if num > 0:
            nums.append(num)
    return sum(nums)

