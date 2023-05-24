"""Kata - Dashatize it

completed at: 2019-05-09 11:37:15
by: Jakub Červinka

Given a variable `n`,

If `n` is an integer,
Return a string with dash``` '-' ```marks before and after each odd integer,  but do not begin or end the string with a dash mark. If `n` is negative, then the negative sign should be removed.

```if:python
If `n` is not an integer, return the string `"None"`.
```
```if:ruby
If `n` is not an integer, return the string `"nil"`.
```
```if:coffeescript,javascript,typescript
If `n` is not an integer, return the string `"NaN"`.
```
```if-not:python,ruby,coffeescript,javascript,typescript
If `n` is not an integer, return an empty value.
```

Ex:
```javascript
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
```
```coffeescript
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
```
```crystal
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
```
```ruby
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
```
```rust
dashatize(274) -> "2-7-4"
dashatize(6815) -> "68-1-5"
```

"""

def dashatize(num):
    if num:
        string = str(abs(num))
        pre_string = ''.join([f'-{ch}-' if int(ch) % 2 == 1 else ch for ch in string])
        truncated = pre_string.replace('--', '-').strip('-')
        return truncated
    else:
        return str(num)
    
    
    
