"""Kata - Find the integer sequences

completed at: 2024-04-16 16:14:07
by: Jakub Červinka

>When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process  --myjinxin2015 said

# Description:
 Complete function `findSequences`. It accepts a positive integer `n`. Your task is to find such integer sequences:

 <span style="background:#000000"><font size=4>Continuous positive integer and their sum value equals to n </font></span>
 
 ```
 For example, n = 15 
 valid integer sequences:
 [1,2,3,4,5]  (1+2+3+4+5==15)
 [4,5,6]          (4+5+6==15)
 [7,8]              (7+8==15)
 
 ```
 The result should be an array `[sequence 1,sequence 2...sequence n]`, sorted by ascending order of the length of sequences; If no result found, return [].
 
  
# Some examples:

```

findSequences(3) === [[1,2]]

findSequences(15) === [[7,8],[4,5,6],[1,2,3,4,5]]

findSequences(20) === [[2, 3, 4, 5, 6]]

findSequences(100) === [[18, 19, 20, 21, 22], [9, 10, 11, 12, 13, 14, 15, 16]]

findSequences(1) === []
```

"""

def find_sequences(n):
    sequences = []
    start = 1
    end = 1
    current_sum = 0
    while start <= n // 2:
        if current_sum < n:
            current_sum += end
            end += 1
        elif current_sum > n:
            current_sum -= start
            start += 1
        else:
            sequences.append(list(range(start, end)))
            current_sum -= start
            start += 1
    return sorted(sequences, key=len)

