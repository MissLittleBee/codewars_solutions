"""Kata - Square Every Digit

completed at: 2024-01-26 15:44:49
by: Jakub Červinka

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9<sup>2</sup> is 81 and 1<sup>2</sup> is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 7<sup>2</sup> is 49, 6<sup>2</sup> is 36, and 5<sup>2</sup> is 25. (49-36-25)

**Note:** The function accepts an integer and returns an integer.

Happy Coding!

"""

def square_digits(num):
    numbers = str(num)
    numberslist = []
    for num in numbers:
        num = int(num)
        num = num ** 2
        num = str(num)
        numberslist.append(num)
    numbers = int("".join(numberslist))
    return numbers
