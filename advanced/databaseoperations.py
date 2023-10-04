#RDBMS

"""
A relational database is a database that organizes information into on eor more data tables

fields: the columns or attributes of the table
records: the rows or observations associated with each field

Remember these tables are related on a key that they both share. In one table, it is called the primary key, in the other table
it is called the foreign key
"""

#Why use Python to access SQLite
"""
SQLite is a lightweight disk-based database meaning we store data on a hard drive or another type of local storage. Many ppl use
sqlite because it doesn't require a separate server process, so programmers can edit or retrieve the data using a nonstandard
form of the SQL query language
"""

import sqlite3
#Syntax for connecting, think of 'sqlite3.connect' as a cable that connects our python environment to our sqlite db
"""
# Create connection to database
connection = sqlite3.connect("first.db")
"""

#Cursor object syntax, imagine a cursor moving back and forth within the cable, communicating to both python and sqlite
"cursor = connection.cursor()"

"""
A cursor object will represent a db cursor, call statements to our sqlite database, and return the data in our python environment
"""

#Executing SQL statements
'''
curs = connection.cursor()
curs.execute("""CREATE TABLE toys (id INTEGER, name TEXT, price REAL, type TEXT)""")
# Insert a row of data in the toys table
curs.execute("""INSERT INTO toys VALUES (2244560, 'Ultimate Ninja Fighter', 24.99, 'action')""")



'''

def helper():
  import sqlite3
  con = sqlite3.connect("titanic.db")
  curs = con.cursor()
  curs.execute('''DROP TABLE IF EXISTS new_table''')
helper()
import sqlite3

con = sqlite3.connect("titanic.db")
curs = con.cursor()

# Create table named new_table
curs.execute("""CREATE TABLE new_table (name TEXT, age INTEGER, username TEXT, pay_rate REAL)""")
# Insert row of values into new_table
curs.execute("""INSERT INTO new_table values ('Bob Peterson', 34, 'bob1234', 40.00)""")