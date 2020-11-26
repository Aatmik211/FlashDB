# FlashDB
Simple NoSQL Key-Value Oriented Database

## USE
```python
>>> db = FlashDB(".db")
>>> db.set(key="name", value="Aatmik")
>>> name = db.get(key="name")
>>> print(name)
Aatmik
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
