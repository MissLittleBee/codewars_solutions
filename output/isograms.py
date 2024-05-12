"""Kata - Isograms

completed at: 2024-03-14 13:30:47
by: Barbora Hůlová

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

**Example: (Input --> Output)**
~~~if-not:factor
```
"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
```
~~~

~~~if:factor
```
"Dermatoglyphics" -> t
"aba" -> f
"moOse" -> f (ignore letter case)
```
~~~
"""

def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True
    
