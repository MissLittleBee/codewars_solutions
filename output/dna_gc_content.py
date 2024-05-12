"""Kata - DNA GC-content

completed at: 2024-03-12 10:41:21
by: Jakub Červinka

The four bases found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).

In genetics, GC-content is the percentage of Guanine (G) and Cytosine (C) bases on a DNA molecule that are either guanine or cytosine. 

Given a DNA sequence (a string) return the GC-content in percent, rounded up to 2 decimal digits for Python, not rounded in all other languages.

For more information about GC-content you can take a look to [wikipedia GC-content](https://en.wikipedia.org/wiki/GC-content).

**For example**: the GC-content of the following DNA sequence is 50%:
"AAATTTCCCGGG".

**Note**: You can take a look to my others bio-info kata [here](http://www.codewars.com/users/nbeck/authored)
"""

def gc_content(seq):
    length = len(seq)
    sum_CG = seq.count("C") + seq.count("G")
    try:
        percentile = round(100 * sum_CG / length,2)
    except:
        percentile = 0
    return percentile
