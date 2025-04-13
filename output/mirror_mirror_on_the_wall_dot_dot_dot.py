"""Kata - Mirror, mirror, on the wall...

completed at: 2025-02-10 11:37:11
by: Barbora Hůlová

## Too long, didn't read

You get a list of integers, and you have to write a function `mirror` that returns the "mirror" (or symmetric) version of this list: i.e. the middle element is the greatest, then the next greatest on both sides, then the next greatest, and so on...


## More info

The list will always consist of integers in range `-1000..1000` and will vary in size between 0 and 10000. Your function **should not mutate the input** array, and this will be tested (where applicable). Notice that the returned list will always be of odd size, since there will always be a definitive middle element.
## Examples

```
[]  -->  []
[1]  -->  [1]
[2, 1]  -->  [1, 2, 1]
[1, 3, 2]  -->  [1, 2, 3, 2, 1]
[-8, 42, 18, 0, -16]  -->  [-16, -8, 0, 18, 42, 18, 0, -8, -16]
[-3, 15, 8, -1, 7, -1] --> [-3, -1, -1, 7, 8, 15, 8, 7, -1, -1, -3]
[-5, 10, 8, 10, 2, -3, 10] --> [-5, -3, 2, 8, 10, 10, 10, 10, 10, 8, 2, -3, -5]
```

Good luck!


~~~if:c
## For C language:
* do not allocate memory for the return value
* assign ints to the provided pointer `*result`

Due to these details, the function should not return anything, so the signature will look like this: 
```c
void mirror(const int *data, size_t n, int *result)
```
where `data` is, of course, an input array (though technically its a pointer to an int), `n` is the size of the array and `result` is the array to which you should assign the resulting elements (again, technically a pointer).
~~~

"""

def mirror(data: list) -> list:
    if not data:
        return []
    
    sorted_data = sorted(data)  
    mirrored = sorted_data + sorted_data[-2::-1]
    return mirrored
