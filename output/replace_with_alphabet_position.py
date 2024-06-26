"""Kata - Replace With Alphabet Position

completed at: 2024-04-14 09:15:14
by: Barbora Hůlová

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

`"a" = 1`, `"b" = 2`, etc.

## Example <!-- unlisted languages will use the first entry. please keep python up top. -->

```python
alphabet_position("The sunset sets at twelve o' clock.")
```
```javascript
alphabetPosition("The sunset sets at twelve o' clock.")
```
```scala
alphabetPosition("The sunset sets at twelve o' clock.")
```
```haskell
alphabetPosition "The sunset sets at twelve o' clock."
```
```cobol
      AlphabetPosition("The sunset sets at twelve o' clock.")
```
```groovy
Kata.alphabetPosition("The sunset sets at twelve o' clock.")
```
```crystal
alphabet_position("The sunset sets at twelve o' clock.")
```
```julia
alphabetposition("The sunset sets at twelve o' clock.")
```
```coffeescript
alphabetPosition("The sunset sets at twelve o' clock.")
```
```crystal
alphabet_position("The sunset sets at twelve o' clock.")
```
```coffeescript
alphabetPosition("The sunset sets at twelve o' clock.")
```
```julia
alphabetposition("The sunset sets at twelve o' clock.")
```
```coffeescript
alphabetPosition("The sunset sets at twelve o' clock.")
```
```csharp
Kata.AlphabetPosition("The sunset sets at twelve o' clock.")
```
```nasm
text:  db  "The sunset sets at twelve o' clock.",0h0

main:
    mov rdi, text
    call alphabet_position
```

Should return `"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"` ( as a string )

"""

def alphabet_position(text):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  new_text = ""
  for char in text:
    if char.lower() in alphabet:
      new_text += str(alphabet.index(char.lower()) + 1) + " "
    else:
      pass
  
  return new_text.strip()

