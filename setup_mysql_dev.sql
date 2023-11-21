#!/usr/bin/python3
"""
Script to prepare MySQL server for the project.

Tasks:
	- Create a database hbnb_test_db
- Create a new user hbnb_test (in localhost)
	- Set the password of hbnb_test to hbnb_test_pwd
	- Grant all privileges to hbnb_test on the database hbnb_test_db (and only this database)
- Grant SELECT privilege to hbnb_test on the database performance_schema (and only this database)
	"""

	import MySQLdb

# Database and user information
	DB_NAME = 'hbnb_test_db'
	DB_USER = 'hbnb_test'
	DB_PASSWORD = 'hbnb_test_pwd'


	try:
	db = MySQLdb.connect(host="localhost", user="root", passwd="")
cursor = db.cursor()


	cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME))


	cursor.execute("CREATE USER IF NOT EXISTS '{}'@'localhost' IDENTIFIED BY '{}'".format(DB_USER, DB_PASSWORD))


	cursor.execute("GRANT ALL PRIVILEGES ON {}.* TO '{}'@'localhost'".format(DB_NAME, DB_USER))


	cursor.execute("GRANT SELECT ON performance_schema.* TO '{}'@'localhost'".format(DB_USER))


	cursor.execute("FLUSH PRIVILEGES")

	cursor.close()
db.close()

	print("MySQL server prepared successfully!")

	except MySQLdb.Error as e:
	print("Error: {}".format(e))
