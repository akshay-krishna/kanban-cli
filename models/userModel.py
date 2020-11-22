import sqlite3
from libs.hash_gen import hash_gen

class UserModel(object):
	"""docstring for UserModel"""
	conn = sqlite3.connect("test.db")

	class User(object):
		def __init__(self, data, conn):	
			self.name = data['name']
			self.u_name = data['u_name']
			self.password = hash_gen(data['password'])
			self.conn = conn
		def save(self):
			print(self.conn)
		def __str__(self):
			return f"{self.name} {self.u_name} {self.password}"

	def __new__(self, data):
		return self.User(data, self.conn)


	@classmethod
	def find_one(cls):
		pass

	@classmethod
	def find_one_and_update(cls):
		pass

	@classmethod
	def delete_one(cls):
		pass