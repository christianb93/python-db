import mysql.connector as dblib

# Determine parameter marker
knownMarkers = {'pyformat' : '%s', 'qmark' : '?'}
marker =  knownMarkers[dblib.paramstyle]
print("Using marker " + marker)


# Get connection to our database. This part is again DB
# specific
c = dblib.connect(user='chr', password='my-secret-pw',
                              host='127.0.0.1',
                              database='books')
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
