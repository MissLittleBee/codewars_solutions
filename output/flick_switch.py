"""Kata - Flick Switch

completed at: 2025-03-27 19:50:38
by: Barbora Hůlová

### Task

Create a function that always returns `True`/`true` for every item in a given list.  
However, if an element is the word **'flick'**, switch to always returning the opposite boolean value.

### Examples

```python
['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]
```

### Notes

- "flick" will always be given in lowercase.
- A list may contain multiple flicks.
- Switch the boolean value on the same element as the flick itself.
"""

def flick_switch(lst):
    state = True
    result = []
    for word in lst:
        if word == "flick":
            state = not state
        result.append(state)
    return result
