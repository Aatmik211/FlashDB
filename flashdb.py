import json
import os

class FlashDB(object):
	"""
	FlashDB is a simple local non-relational database management system.
	FlashDB database files end with a '.db' extension.
	Currently, FlashDB has 4 functions:
	  set - saves a value to the database
	  get - retrieves a value from the database
	  delete - deletes a value from the database
	  reset - resets the database, i.e., erases all data from it

	Usage:
	  new_flashdb_instance = FlashDB("location/to/database/file/.db")
	  new_flashdb_instance.set(key, value)
	  new_flashdb_instance.get(key)

	Example:
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
	"""
	def __init__(self, location):
		self.location = os.path.expanduser(location)
		self.load(self.location)

	def load(self, location):
		if os.path.exists(location):
			self._load()
		else:
			self.db = {}
		return True

	def _load(self):
		self.db = json.load(open(self.location, 'r'))

	def dumpdb(self):
		try:
			json.dump(self.db, open(self.location, 'w+'), indent=4)
			return True
		except:
			return False

	def set(self, key, value):
		try:
			self.db[str(key)] = value
			self.dumpdb()
			return True
		except Exception:
			print("[X] Error Saving Values To Database")
			return False
	
	def get(self, key):
		try:
			return self.db[str(key)]
		except KeyError:
			print(f"[X] Invalid Key-ID: {key}")
			return False

	def delete(self, key):
		if not key in self.db:
			print(f"[X] Invalid Key-ID: {key}")
			return False
		del self.db[str(key)]
		return True

	def reset(self):
		self.db = {}
		self.dumpdb()
		print("[O] Reset Successfull")
		return True
