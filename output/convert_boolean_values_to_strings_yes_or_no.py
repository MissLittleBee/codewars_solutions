"""Kata - Convert boolean values to strings 'Yes' or 'No'.

completed at: 2022-07-20 14:06:43
by: Jakub Červinka

Complete the method that takes a boolean value and return a `"Yes"` string for `true`, or a `"No"` string for `false`.

"""

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
