# sql.py - Create a SQLite3 table and populate witrh data 

import sqlite3

# create a new database if the database doesnt already exist 
with sqlite3.connect("blog.db") as connection:
	#get a  cursor 
	c = connection.cursor()

	#create the table
	#c.execute("""CREATE TABLE posts 		(title TEXT,post TEXT)		""")
	# insert dummy data into the table 
	c.execute('INSERT INTO posts VALUES("Good","iyiyim.")')
	c.execute('INSERT INTO posts VALUES("Well","cok iyiyim.")')
	c.execute('INSERT INTO posts VALUES("Excellent","Hee mukemmel iyiyim.")')
	c.execute('INSERT INTO posts VALUES("Okay","Sahane iyiyim.")')
