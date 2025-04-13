"""Kata - Check same case

completed at: 2025-04-13 14:53:51
by: Barbora Hůlová

Write a function that will check if two given characters are the same case.

* If either of the characters is not a letter, return `-1`
* If both characters are the same case, return `1`
* If both characters are letters, but not the same case, return `0`

## Examples

`'a'` and `'g'` returns `1`

`'A'` and `'C'` returns `1`

`'b'` and `'G'` returns `0`

`'B'` and `'g'` returns `0`

`'0'` and `'?'` returns `-1`
"""

def same_case(a, b): 
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vals = (a.isupper(),b.isupper(), a in chars and b in chars)
    return{
        (True,True,True): 1,
        (False,False,True):1,
        (False,True,True): 0, 
        (True,False,True): 0,
        (False,True,False): -1, 
        (True,False,False): -1,
        (True,True,False): -1,
        (False,False,False): -1,
    }[vals]

        
    
