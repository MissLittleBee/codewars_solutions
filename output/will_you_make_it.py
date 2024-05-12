"""Kata - Will you make it?

completed at: 2022-06-22 10:17:40
by: Jakub Červinka

You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is `50` miles away! You know that on average, your car runs on about `25` miles per gallon. There are `2` gallons left. 

Considering these factors, write a function that tells you if it is possible to get to the pump or not.

```if-not:prolog,nasm,cobol
Function should return `true` if it is possible and `false` if not.
```

```if:prolog,nasm,cobol
Function should return `1` if it is possible and `0` if not.
```

"""

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump :
        return True
    else:
        return False
        
