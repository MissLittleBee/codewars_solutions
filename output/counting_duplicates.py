"""Kata - Counting Duplicates

completed at: 2024-04-12 18:36:06
by: Barbora Hůlová

### Count the number of Duplicates

Write a function that will return the count of **distinct case-insensitive** alphabetic characters and numeric digits that occur more than 
once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.


### Example
"abcde" -> 0             `# no characters repeats more than once`  
"aabbcde" -> 2           `# 'a' and 'b'`  
"aabBcde" -> 2           ``# 'a' occurs twice and 'b' twice (`b` and `B`)``  
"indivisibility" -> 1    `# 'i' occurs six times`  
"Indivisibilities" -> 2  `# 'i' occurs seven times and 's' occurs twice`  
"aA11" -> 2              `# 'a' and '1'`  
"ABBA" -> 2              `# 'A' and 'B' each occur twice`

"""

def duplicate_count(text):
    if text == '':
        return 0
    else:
        text = text.lower()
        print(text)
        duplicates = []
        for char in text:
            if text.count(char) > 1 and char not in duplicates:
                duplicates.append(char)

    return len(duplicates)
        
        
     
