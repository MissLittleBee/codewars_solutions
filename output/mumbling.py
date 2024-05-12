"""Kata - Mumbling

completed at: 2024-03-14 12:17:31
by: Barbora Hůlová

This time no story, no theory. The examples below show you how to write function `accum`:

#### Examples:
```
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
```

The parameter of accum is a string which includes only letters from `a..z` and `A..Z`.
"""

def accum(st):
    new_str =[]
    n=1
    for i in st:
        new_str.append((i*n).capitalize())  # Přidání metody capitalize()
        n+=1
    new_str = '-'.join(new_str)
    return str(new_str)
