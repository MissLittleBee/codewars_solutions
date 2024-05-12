"""Kata - Welcome to the City

completed at: 2022-06-10 13:43:23
by: Jakub Červinka

Create a method that takes as input a name, city, and state to welcome a person. Note that `name` will be an array consisting of one or more values that should be joined together with one space between each, and the length of the `name` array in test cases will vary.

Example:

```
['John', 'Smith'], 'Phoenix', 'Arizona'
```

This example will return the string `Hello, John Smith! Welcome to Phoenix, Arizona!`

"""

def say_hello(name, city, state):
    name = " ".join(name)
    return f"Hello, {name}! Welcome to {city}, {state}!"
