import MySQLdb as mdb

class Database:
	def __init__(self, server, username, password, db):
		try:
			self.Connection = mdb.connect(server, username, password, db)
			self.Cursor = self.Connection.cusror()
		except mdbError e:
			print "Error {}: {}".format(e.args[0], e.args[1])
		finally:
			if self.Connection:
				self.Connection.close()
