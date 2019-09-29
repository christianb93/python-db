import sqlite3 as dblib
from pathlib import Path

# Get connection to our database. This part is again DB
# specific
home = str(Path.home())
db = home + "/example.db"
c = dblib.connect(db)

# Open cursor. Everything below this line should be
# the same for all databases
cursor = c.cursor()

# Get all rows from table books
statement = "SELECT author, title from books;"
cursor.execute(statement)
rows = cursor.fetchall()

# Iterate through result set
for row in cursor:
    print ("Author: " + row[0])
    print ("Title:  " + row[1])
