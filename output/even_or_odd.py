"""Kata - Even or Odd

completed at: 2024-01-21 12:42:37
by: Jakub Červinka

~~~if-not:sql,shell
Create a function that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.
~~~

~~~if:sql
You will be given a table `numbers`, with one column `number`.</br>

Return a dataset with two columns: `number` and `is_even`, where `number` contains the original input value, and `is_even` containing `"Even"` or `"Odd"` depending on `number` column values.

### Numbers table schema

```text
* number INT
```

### Output table schema

```text
* number  INT
* is_even STRING
```
~~~

~~~if:shell
Write a script that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.
~~~

"""

def even_or_odd(number):
    moduloresult = number % 2
    if moduloresult == 0:
        return "Even"
    else: return "Odd"
    pass
