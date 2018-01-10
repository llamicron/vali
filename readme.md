# Vali
## Easy type checking
```python
from vali import validate

results = validate({
    int: 45,
    str: 'string',
    float: 42.9,
    tuple: ('first', 'second')
})

print(results) # True

results = validate({
    int: '45',
    str: ('first', 'second'),
    float: ['list', 'of', 'items'],
    tuple: 45
})

print(results) # False
```

## Additional Options
You can add two more paramaters to `validate`.
### `return_failures`
```python
to_validate = {
    int: 'not an int',
    list: 100
}
results = validate(to_validate, return_failures=True)

print(results)
```

returns a list of tuples, containing the type and the value

```python
[(<class 'int'>, 'not an int'), (<class 'list'>, 100)]
```

### `raise_on_failure`
```python
to_validate = {
    int: 'not an int'
}

validate(to_validate, raise_on_failure=True) # This will throw a ValidationError
```
Will throw a `ValidationError`. Note: `ValidationError` extends `ValueError`. That may be useful when catching this error.

## Notes
The entended way for this to be used is like so:
```python
items = {
    int: 14,
    str: 'some string'
}

if not validate(items): # Validation did not pass
    # Deal with this
```
But remember, if you have the `return_failures` set to `True`, then that test will pass. See here:
```python
items = {
    int: 14,
    str: 'some string'
}

if not validate(items, return_failures): # Validation DID pass
    # Continue
```
