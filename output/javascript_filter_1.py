"""Kata - Javascript filter - 1

completed at: 2024-03-12 10:09:57
by: Barbora Hůlová

While developing a website, you detect that some of the members have troubles logging in. Searching through the code you find that all logins ending with a "\_" make problems. So you want to write a function that takes an array of pairs of login-names and e-mails, and outputs an array of all login-name, e-mails-pairs from the login-names that end with "\_".

If you have the input-array:

```
[ [ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
```

it should output

```
[ [ "bar_", "bar@bar.com" ] ]
```

You *have to* use the *filter*-method which returns each element of the array for which the *filter*-method returns true.

```javascript
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
```

```python
https://docs.python.org/3/library/functions.html#filter
```
"""

def search_names(logins):
  def filter_login(login_email):
    return login_email[0].endswith('_')
  return list(filter(filter_login, logins))
