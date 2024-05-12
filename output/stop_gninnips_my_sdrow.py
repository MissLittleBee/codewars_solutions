"""Kata - Stop gninnipS My sdroW!

completed at: 2024-01-26 14:52:38
by: Jakub Červinka

Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:
```
"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
```
"""

def spin_words(sentence):
    if " " in sentence:
        words = sentence.split(" ")
        new_words = []
        for word in words:
            if len(word) > 4:
                word = word[::-1]
            new_words.append(word)
        sentence = " ".join(new_words)
    else:
        if len(sentence) > 4:
            sentence = sentence[::-1]
    return sentence
