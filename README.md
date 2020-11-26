# FlashDB
Simple NoSQL key-value oriented database

## USE
```python
>>> db = FlashDB(".db")
>>> db.set(key="name", value="John")
>>> name = db.get(key="name")
>>> print(name)
John
>>> db.set(key="fav_col", value="Green")
>>> fav_col = db.get(key="fav_col")
>>> print(fav_col)
Green
>>> db.delete(key="fav_col")
>>> fav_col = db.get(key="fav_col")
[X] Invalid Key-ID: fav_col
>>> db.reset()
[O] Reset Successfull
>>> name = db.get(key="name")
[X] Invalid Key-ID: name
```
