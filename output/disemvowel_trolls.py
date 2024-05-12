"""Kata - Disemvowel Trolls

completed at: 2024-01-21 13:57:25
by: Barbora Hůlová

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata `y` isn't considered a vowel.

"""

def disemvowel(string_):
    spells = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for spell in spells:
        string_ = string_.replace(spell, "")
    return string_

