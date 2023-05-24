"""Kata - Lazy Repeater

completed at: 2022-10-09 19:43:25
by: Jakub Červinka

The `makeLooper()` function (`make_looper` in Python) takes a string (of non-zero length) as an argument.  It returns a function.  The function it returns will return successive characters of the string on successive invocations.  It will start back at the beginning of the string once it reaches the end.

For example:
```javascript
var abc = makeLooper('abc');
abc(); // should return 'a' on this first call
abc(); // should return 'b' on this second call
abc(); // should return 'c' on this third call
abc(); // should return 'a' again on this fourth call
```
```coffeescript
abc = makeLooper 'abc'
abc() # should return 'a' on this first call
abc() # should return 'b' on this second call
abc() # should return 'c' on this third call
abc() # should return 'a' again on this fourth call
```
```csharp
Func<char> abc = Kata.MakeLooper("abc");
abc(); // should return 'a' on this first call
abc(); // should return 'b' on this second call
abc(); // should return 'c' on this third call
abc(); // should return 'a' again on this fourth call
```
```python
abc = make_looper('abc')
abc() # should return 'a' on this first call
abc() # should return 'b' on this second call
abc() # should return 'c' on this third call
abc() # should return 'a' again on this fourth call
```
"""

from itertools import cycle
def make_looper(string):
    c = cycle(string)
    def foo():
        return next(c)
    foo.__name__ = string
    return foo

