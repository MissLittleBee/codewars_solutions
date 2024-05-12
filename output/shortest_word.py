"""Kata - Shortest Word

completed at: 2024-04-14 08:59:19
by: Jakub Červinka

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

"""

def find_short(s):
    words = s.split()
    shortest = 20
    for w in words:
        if len(w) < shortest:
            shortest = len(w)
    return shortest
        
