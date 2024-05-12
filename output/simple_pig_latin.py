"""Kata - Simple Pig Latin

completed at: 2024-04-16 15:35:08
by: Jakub Červinka

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

## Examples

```javascript
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !
```
```objc
pigIt(@"Pig latin is cool"); // => @"igPay atinlay siay oolcay"
pigIt(@"Hello world !");     // => @"elloHay orldway !"
```
```ruby
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
```
```python
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
```
```csharp
Kata.PigIt("Pig latin is cool"); // igPay atinlay siay oolcay
Kata.PigIt("Hello world !");     // elloHay orldway !
```
```C++
pig_it("Pig latin is cool");   // igPay atinlay siay oolcay
pig_it("Hello world !");       // elloHay orldway
```
```Java
PigLatin.pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
PigLatin.pigIt('Hello world !');     // elloHay orldway !
```
```clojure
(piglatin/pig-it "Pig latin is cool") ; "igPay atinlay siay oolcay"
(piglatin/pig-it "Hello world !")     ; "elloHay orldway !"
```
```typescript
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !
```
```cobol
      PigIt str = 'Pig latin is cool' => result = 'igPay atinlay siay oolcay'
      PigIt str = 'Hello world !'     => result = 'elloHay orldway !
```

"""

def pig_it(text):
  words = text.split(' ')
  new_words = []
  for word in words:
    punct = '' 
    if word[-1] in ',.?!':
      punct = word[-1]
      word = word[:-1] 
    if word:
      new_words.append(word[1:] + word[0] + 'ay')
    new = ' '.join(new_words)
  if punct:
    return new + ' ' + punct
  else:
    return new


