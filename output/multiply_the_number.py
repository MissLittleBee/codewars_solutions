"""Kata - Multiply the number

completed at: 2024-01-21 13:04:49
by: Jakub Červinka

Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:

```
  3 -->    15  (  3 * 5¹)
 10 -->   250  ( 10 * 5²)
200 --> 25000  (200 * 5³)
  0 -->     0  (  0 * 5¹)
 -3 -->   -15  ( -3 * 5¹)
```
"""

def multiply(n):
    result = n* 5
    return n * (5 ** len(str(abs(n))))
        
    pass
