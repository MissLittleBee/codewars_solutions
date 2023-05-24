"""Kata - Plus - minus - plus - plus - ... - Count

completed at: 2019-02-24 17:52:44
by: Jakub Červinka

Count how often sign changes in array.

### result
number from `0` to ... . Empty array returns `0`

### example
```javascript
const arr = [1, -3, -4, 0, 5];

/*
| elem | count |
|------|-------|
|  1   |  0    |
| -3   |  1    |
| -4   |  1    |
|  0   |  2    |
|  5   |  2    |
*/

catchSignChange(arr) == 2;
```
"""

def catch_sign_change(lst):
    from itertools import groupby
    return 0 if len(lst) == 0 else len([sum(g) for _, g in groupby(lst, key=lambda x: x < 0)])-1
