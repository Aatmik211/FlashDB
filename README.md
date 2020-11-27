# FlashDB
FlashDB is a simple local NoSQL key-value oriented database management system.
FlashDB database files end with a '.db' extension.
Currently, FlashDB has 4 functions:

```
set - saves a value to the database
get - retrieves a value from the database
delete - deletes a value from the database
reset - resets the database, i.e., erases all data from it
```

## USE:
```python
new_flashdb_instance = FlashDB("location/to/database/file/.db")
new_flashdb_instance.set(key, value)
new_flashdb_instance.get(key)
```

## EXAMPLE:
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
