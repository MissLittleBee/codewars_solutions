"""Kata - Cogs 2

completed at: 2024-04-09 20:31:00
by: Jakub Červinka

<img src="http://bestanimations.com/Science/Gears/loadinggears/loading-gears-animation-6-4.gif"/>

# Kata Task

You are given a list of cogs in a <a href ="https://en.wikipedia.org/wiki/Gear_train">gear train</a>

Each element represents the number of teeth of that cog

e.g. `[100, 50, 25]` means 
* 1st cog has 100 teeth 
* 2nd cog has 50 teeth
* 3rd cog has 25 teeth

If the ``nth`` cog rotates clockwise at 1 RPM what is the RPM of the cogs at each end of the gear train? 

**Notes**
* no two cogs share the same shaft
* return an array whose two elements are RPM of the first and last cogs respectively
* use negative numbers for anti-clockwise rotation
* for convenience `n` is zero-based
* For C and NASM coders, the returned array will be `free`'d.

---

Series:
* <a href=https://www.codewars.com/kata/cogs>Cogs</a>
* Cogs 2

"""

def process_wheels(whls):
    rpm = 1
    for i, w in enumerate(whls[:-1]):
        rpm *= -w / whls[i + 1]
    return rpm

def cog_RPM(cogs, n):
    return [
        process_wheels(cogs[:n+1][::-1]),
        process_wheels(cogs[n:])
    ]
