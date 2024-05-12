"""Kata - Area of a Square

completed at: 2022-06-10 14:36:14
by: Barbora Hůlová

Complete the function that calculates the area of the red square, when the length of the circular arc `A` is given as the input. Return the result rounded to two decimals.

![Graph](http://i.imgur.com/nJrae8n.png)

Note: use the π value provided in your language (`Math::PI`, `M_PI`, `math.pi`, etc)
"""

from math import pi

def square_area(A):
    return round((A*2/pi)**2,2)
    
