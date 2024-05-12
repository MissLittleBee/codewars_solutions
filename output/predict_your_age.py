"""Kata - Predict your age!

completed at: 2022-07-22 10:43:47
by: Barbora Hůlová

My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!

In honor of my grandfather's memory we will write a function using his formula!

* Take a list of ages when each of your great-grandparent died.  
* Multiply each number by itself.  
* Add them all together.  
* Take the square root of the result.  
* Divide by two.

## Example

```javascript
predictAge(65, 60, 75, 55, 60, 63, 64, 45) === 86
```
```R
predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
```
```python
predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
```
```ruby
predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
```
```crystal
predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
```
```c++
predictAge(65, 60, 75, 55, 60, 63, 64, 45) == 86
```
```php
predictAge(65, 60, 75, 55, 60, 63, 64, 45) == 86
```
```csharp
predictAge(65, 60, 75, 55, 60, 63, 64, 45) == 86
```
```lua
Predicter.predictAge(65, 60, 75, 55, 60, 63, 64, 45) == 86
```



Note: the result should be rounded down to the nearest integer.

Some random tests might fail due to a bug in the JavaScript implementation. Simply resubmit if that happens to you.
"""

import math
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    list_age = []
    list_age.extend([age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8])
    mult_list = []
    for i in range(len(list_age)):
        n = list_age[i] * list_age[i]
        mult_list.append(n)
    suma = sum(mult_list)
    age = math.sqrt(suma) / 2
    return round_down(age)
        
        
