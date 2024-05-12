"""Kata - Get the Middle Character

completed at: 2024-04-12 14:19:17
by: Barbora Hůlová

You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

```
Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"

```




#Input


A word (string) of length `0 < str < 1000` (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.



#Output


The middle character(s) of the word represented as a string.

"""

def get_middle(word):
    middle_list = []
    if len(word) == 1:  
        return word

    middle_length = len(word) // 2
    if middle_length * 2 == len(word):
        left_middle_index = middle_length - 1
        right_middle_index = middle_length
        middle_list.extend([word[left_middle_index], word[right_middle_index]])
    else:  
        middle_index = middle_length
        middle_list.extend([word[middle_index]])
    return ''.join(middle_list)

