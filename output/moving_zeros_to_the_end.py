"""Kata - Moving Zeros To The End

completed at: 2024-04-12 19:32:49
by: Barbora Hůlová

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

```php
moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]
```
```javascript
moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]
```
```python
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
```
```cpp
move_zeros({1, 0, 1, 2, 0, 1, 3}) // returns {1, 1, 2, 1, 3, 0, 0}
```
```coffeescript
moveZeros [false,1,0,1,2,0,1,3,"a"] # returns[false,1,1,2,1,3,"a",0,0]
```
```csharp
Kata.MoveZeroes(new int[] {1, 2, 0, 1, 0, 1, 0, 3, 0, 1}) => new int[] {1, 2, 1, 1, 3, 1, 0, 0, 0, 0}
```
```go
MoveZeros([]int{1, 2, 0, 1, 0, 1, 0, 3, 0, 1}) // returns []int{ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 }
```
```haskell
moveZeros [1,2,0,1,0,1,0,3,0,1] -> [1,2,1,1,3,1,0,0,0,0]
```
```factor
{ 1 2 0 1 0 1 0 3 0 1 } move-zeros -> { 1 2 1 1 3 1 0 0 0 0 }
```
```ruby
moveZeros [1,2,0,1,0,1,0,3,0,1] #-> [1,2,1,1,3,1,0,0,0,0]
```
```c
move_zeros(10, int [] {1, 2, 0, 1, 0, 1, 0, 3, 0, 1}); // -> int [] {1, 2, 1, 1, 3, 1, 0, 0, 0, 0}
```
```scala
moveZeroes(List(1, 0, 1, 2, 0, 1, 3)) // -> List(1, 1, 2, 1, 3, 0, 0)
```
```bf
"1012013\0"   -->   "1121300"
```
"""

def move_zeros(lst):
  j = 0
  for i in range(len(lst)):
    if lst[i] != 0:
      lst[i], lst[j] = lst[j], lst[i]
      j += 1
  return lst

