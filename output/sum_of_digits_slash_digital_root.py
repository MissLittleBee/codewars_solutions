"""Kata - Sum of Digits / Digital Root

completed at: 2024-01-26 16:28:33
by: Jakub Červinka

[Digital root](https://en.wikipedia.org/wiki/Digital_root) is the _recursive sum of all the digits in a number._

Given `n`, take the sum of the digits of `n`. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

## Examples
```
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
```

"""

def digital_root(n):
    n = n
    while len(str(n)) >= 2:
        num_list = []
        n = str(n)
        for num in n:
            num_list.append((int(num)))
        n = sum(num_list)
    return int(n)

