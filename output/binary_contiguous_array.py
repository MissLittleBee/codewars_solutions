"""Kata - Binary Contiguous Array

completed at: 2024-04-25 19:53:56
by: Jakub Červinka

An array consisting of `0`s and `1`s, also called a binary array, is given as an input.

### Task

Find the length of the longest contiguous subarray which consists of **equal** number of `0`s and `1`s.

### Example

```
s = [1,1,0,1,1,0,1,1]
         |_____|
            |
         [0,1,1,0]

         length = 4
```

### Note

<!-- this should show the first block for every language except LC -->
```c
0 <= length(array) < 120 000
```
```lambdacalc
0 <= length list <= 25
```

~~~if:lambdacalc
### Encodings

purity: `LetRec`  
numEncoding: `BinaryScott`  
export constructors `nil, cons` for your `List` encoding  
~~~
"""

def binarray(arr):
    count = 0
    map = {0: -1}
    max_length = 0

    arr = [1 if x else -1 for x in arr]

    for i, number in enumerate(arr):
        count += number

        if count in map:
            max_length = max(max_length, (i - map[count]))
        else:
            map[count] = i

    return max_length

