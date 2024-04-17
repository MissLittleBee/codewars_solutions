"""Kata - Real Password Cracker

completed at: 2024-04-16 18:23:59
by: Jakub Červinka

### Story

You are a h4ck3r n00b: you "acquired" a bunch of password hashes, and you want to decypher them. Based on the length, you already guessed that they must be SHA-1 hashes. You also know that these are weak passwords: maximum 5 characters long and use only lowercase letters (`a-z`), no other characters.

Happy hacking!

**Notes:**
* pre-generating the full hash table is not advised, due to the time-limit on the CW platform
* there will be only a few tests for 5-letter words *(hint: start from the beginning of the alphabet)*
* if your solution times out, try running it again - the CW runner is sometimes a bit slow(er)

---

### My other katas

If you enjoyed this kata then please try [my other katas](https://www.codewars.com/users/anter69/authored)! :-)

#### *Translations are welcome!*
"""

from hashlib import sha1
from itertools import product
from string import ascii_lowercase as al

def password_cracker(hash):
    for l in range(1, 6):
        for word in product(al, repeat=l):
            word = ''.join(word)
            if sha1(word.encode()).hexdigest() == hash:
                return word
