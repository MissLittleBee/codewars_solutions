"""Kata - Your order,  please

completed at: 2024-04-19 15:06:13
by: Jakub Červinka

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.


## Examples

```
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
```
"""

def order(sentence):
    sentence = sentence.split(' ')
    num = '1,2,3,4,5,6,7,8,9'
    new_s = []
    for num in num:
        for word in sentence:
            if num in word:
                new_s.append(word)
    return ' '.join(new_s)
