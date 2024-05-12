"""Kata - Convert a string to an array

completed at: 2022-06-09 08:40:31
by: Jakub Červinka

Write a function to split a string and convert it into an array of words.

### Examples (Input ==> Output):

```
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
```

```if:c
Words will be separated by exactly one space, without leading or trailing spaces.

There will only be letters and spaces in the input string.
```

"""

def string_to_array(s):
    return s.split(" ")
