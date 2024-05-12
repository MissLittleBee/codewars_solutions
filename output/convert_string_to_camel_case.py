"""Kata - Convert string to camel case

completed at: 2024-04-17 15:12:11
by: Jakub Červinka

Complete the method/function so that it converts dash/underscore delimited words into [camel casing](https://en.wikipedia.org/wiki/Camel_case). The first word within the output should be capitalized **only** if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

### Examples

`"the-stealth-warrior"` gets converted to `"theStealthWarrior"` 
 
`"The_Stealth_Warrior"` gets converted to `"TheStealthWarrior"`

`"The_Stealth-Warrior"` gets converted to `"TheStealthWarrior"`

"""

def to_camel_case(text):
  sep = "!#%&?-_ "
  new_s = text
  while True:
    for char in sep:
      if char in new_s:
        ind = new_s.index(char)
        new_s = new_s[:ind] + new_s[ind+1].upper() + new_s[ind+2:]
        break
    else:
      break
  return new_s

            
