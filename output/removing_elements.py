"""Kata - Removing Elements

completed at: 2022-06-09 08:57:35
by: Barbora Hůlová

Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

### Example:

```if-not:c
`["Keep", "Remove", "Keep", "Remove", "Keep", ...]` --> `["Keep", "Keep", "Keep", ...]`
```

```if:c
~~~c
size_t length = 5;
remove_every_other(&length, {1, 2, 3, 4, 5});
// -->  {1, 3, 5}
~~~
```

None of the arrays will be empty, so you don't have to worry about that!

"""

def remove_every_other(my_list):
    del my_list[1::2]
    return my_list
