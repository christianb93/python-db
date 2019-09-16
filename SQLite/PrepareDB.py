import sqlite3 as dblib
from pathlib import Path


# Determine parameter marker
knownMarkers = {'pyformat' : '%s', 'qmark' : '?'}
marker =  knownMarkers[dblib.paramstyle]
print("Using marker " + marker)


# Get connection to our database. This part is again DB
# specific
home = str(Path.home())
db = home + "/example.db"
print ("Using database at", db)
c = dblib.connect(db)


# Open cursor. Everything below this line should be
# the same for all databases
cursor = c.cursor()

# Now create a table books. We first try to drop the table
# if it exists
try:
    cursor.execute('''DROP TABLE books''')
except dblib.Error as err:
    pass

# Now create it
cursor.execute('''CREATE TABLE books
             (author text, title text)''')

# Next let us insert some sample records

examples = [('Dickens', 'David Copperfield'),
            ('Melville', 'Moby Dick')]

# Be careful - MySQL uses %s as parameter markes, while SQLLite3
# uses ?. We therefore use the marker determined above
sqlString =  '''INSERT INTO books
                       (author, title)
                 VALUES ''' + "(" + marker + "," + marker + ")"
cursor.executemany(sqlString, examples)

# and commit
c.commit()


# Finally close connection again
c.close()
