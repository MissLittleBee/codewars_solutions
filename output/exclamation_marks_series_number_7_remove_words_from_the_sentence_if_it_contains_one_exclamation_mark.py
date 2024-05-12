"""Kata - Exclamation marks series #7: Remove words from  the sentence if it contains one exclamation mark 

completed at: 2022-05-31 12:19:43
by: Barbora Hůlová

# Description:

Remove words from the sentence if they contain exactly one exclamation mark. Words are separated by a single space, without leading/trailing spaces.

# Examples

```
remove("Hi!") === ""
remove("Hi! Hi!") === ""
remove("Hi! Hi! Hi!") === ""
remove("Hi Hi! Hi!") === "Hi"
remove("Hi! !Hi Hi!") === ""
remove("Hi! Hi!! Hi!") === "Hi!!"
remove("Hi! !Hi! Hi!") === "!Hi!"
```

"""

def remove(s):
    correct_w = []
    words = s.split()
    for word in s.split():
         if word.count('!') != 1:
            correct_w.append(word)
    return ' '.join(correct_w)
