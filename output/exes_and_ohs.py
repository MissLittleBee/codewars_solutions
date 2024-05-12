"""Kata - Exes and Ohs

completed at: 2024-04-12 19:02:33
by: Barbora Hůlová

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:
```
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
```
"""

def xo(s):
    s= s.lower()
    if 'x' and 'o' not in s:
        return True
    elif s.count('x') == s.count('o'):
        return True
    else:
        return False
