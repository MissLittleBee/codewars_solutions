"""Kata - reverseIt

completed at: 2025-02-10 10:54:34
by: Barbora Hůlová

You have to create a function named reverseIt.

Write your function so that in the case a string or a number is passed in as the data , you will return the data in reverse order. If the data is any other type, return it as it is.


Examples of inputs and subsequent outputs:
```
"Hello" -> "olleH"

"314159" -> "951413"

[1,2,3] -> [1,2,3]
```
"""

def reverse_it(data):
    if isinstance(data, str):
        return data[::-1]
    elif isinstance(data, int) and not isinstance(data, bool):
        return int(str(data)[::-1])
    elif isinstance(data, float):
        # Reverse the string representation and convert back to float
        reversed_str = str(data)[::-1]
        return float(reversed_str)
    else:
        return data
