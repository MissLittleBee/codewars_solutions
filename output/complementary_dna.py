"""Kata - Complementary DNA

completed at: 2024-04-16 13:38:17
by: Jakub Červinka

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (**input --> output**)
~~~if-not:haskell
```
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
```
~~~
```if:haskell
dnaStrand []        `shouldBe` []
dnaStrand [A,T,G,C] `shouldBe` [T,A,C,G]
dnaStrand [G,T,A,T] `shouldBe` [C,A,T,A]
dnaStrand [A,A,A,A] `shouldBe` [T,T,T,T]
```

"""

def DNA_strand(dna):
    new_s = []
    for char in dna:
        if char == 'A':
            new_s.append('T')
        elif char == 'T':
            new_s.append('A')
        elif char == 'G':
            new_s.append('C')
        elif char == 'C':
            new_s.append('G')
    return ''.join(new_s) 
