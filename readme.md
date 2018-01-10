# Vali
## Easy type checking
```python
from vali import validate

foo = 'string'
bar = 16
baz = ('string', 3)

results = validate(dict(
    'str': foo,
    'int': bar,
    'tuple': baz
))

if not results:
    print("Ahhh")
```

It can also throw an exception if you want:
```python
from vali import validate

foo = 'string'
bar = 16
baz = ('string', 3)

results = validate(dict(
    'tuple': foo, # This will throw an exception
    'int': bar,
    'tuple': baz
), return_type='Exception')
```
