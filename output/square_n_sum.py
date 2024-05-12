"""Kata - Square(n) Sum

completed at: 2022-06-08 15:05:07
by: Barbora Hůlová

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for `[1, 2, 2]` it should return `9` because `$1^2 + 2^2 + 2^2 = 9$`.

```if:racket
In Racket, use a list instead of an array, so '(1 2 2) should return 9.
```

"""

def square_sum(numbers):
    for numb in numbers:
        ind = numbers.index(numb)
        numb = numb**2
        numbers[ind] = numb
    return(sum(numbers))
