"""Kata - If you can't sleep, just count sheep!!

completed at: 2022-08-11 07:53:37
by: Jakub Červinka

If you can't sleep, just count sheep!!

## Task:
Given a non-negative integer, `3` for example, return a string with a murmur: `"1 sheep...2 sheep...3 sheep..."`.  Input will always be valid, i.e. no negative integers.

"""

def count_sheep(n):
    list_str = []
    for i in range(1,n+1):
        str = f"{i} sheep..."
        list_str.append(str)
    return "".join(list_str)
    
