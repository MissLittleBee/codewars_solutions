"""Kata - Credit Card Mask

completed at: 2024-04-16 15:58:04
by: Jakub Červinka

Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function `maskify`, which changes all but the last four characters into `'#'`.

## Examples (input --> output):
```
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"
"Skippy" --> "##ippy"
"Nananananananananananananananana Batman!" --> "####################################man!"
```

"""

def maskify(cc):
  if len(cc) > 4:
    mask_length = len(cc) - 4
    masked_cc = ''
    for i in range(len(cc)):
      if i < mask_length:
        masked_cc += '#'
      else:
        masked_cc += cc[i]
    return masked_cc
  else:
    return cc

