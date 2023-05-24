"""Kata - Scramblies

completed at: 2019-04-19 17:03:50
by: Jakub Červinka

Complete the  function `scramble(str1, str2)` that returns `true` if a portion of ```str1``` characters can be rearranged to match ```str2```, otherwise returns ```false```.

**Notes:**
* Only lower case letters will be used (a-z). No punctuation or digits will be included.
* Performance needs to be considered.

```if:c
* Input strings s1 and s2 are null terminated.
```

## Examples

```python
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
```

"""

def scramble(s1, s2):
    from collections import Counter  
    return len(Counter(s2) - Counter(s1)) == 0
