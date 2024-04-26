"""Kata - Simple Sum (with restrictions)

completed at: 2024-04-25 19:20:50
by: Jakub Červinka

## Task

You're given two non-negative numbers `(0 <= x,y)`. The goal is to create a function named `simple_sum` which return their sum.

## Restrictions

The restrictions can be summurized as 'bit and logical operations are allowed'.

Here comphrensive description. You're code __mustn't__ contain:

```
1. `import`, `getattr`, `exec`, `eval`, `sum`  # with next point produce short solutions,
2. `int` class methods names                   # but here is another idea.
3. `__loader__`, `vars`, `__dict__`            # even more of them.
4. `if`, `in`, `is`                            # they start with `i` :)
5. `+`, `-`, `*`, `/`, `//`, `%`               # arithmetic operations
6. `==`, `!=`, `<`, `>`, `<=`, `>=`            # comparisions
```

## Note

**Inspired by [suic](https://www.codewars.com/users/553bfb4e8234ef15340000b9)'s katas**

**Please  assess the difficulty  of the kata when you finish it :)**
"""

def simple_sum(a, b):
    while b:
        swc = a ^ b
        carry = (a & b) << 1
        a, b = swc, carry
    return a
