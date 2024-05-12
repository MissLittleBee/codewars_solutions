"""Kata - Descending Order

completed at: 2024-03-12 12:18:35
by: Jakub Červinka

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.


### Examples:

Input: `42145`
Output: `54421`

Input: `145263`
Output: `654321`

Input: `123456789`
Output: `987654321`


"""

def descending_order(num):
    nums = str(num)
    sorted_nums = sorted(nums, reverse = True)
    num = ''.join(sorted_nums)
    return int(num)
