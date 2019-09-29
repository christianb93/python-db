import mysql.connector as dblib

# Get connection to our database. This part is again DB
# specific
c = dblib.connect(user='chr', password='my-secret-pw',
                              host='127.0.0.1',
                              database='books')

# Open cursor. Everything below this line should be
# the same for all databases
cursor = c.cursor()

# Get all rows from table books
statement = "SELECT author, title from books;"
cursor.execute(statement)
rows = cursor.fetchall()

# Iterate through result set
for row in rows:
    print ("Author: " + row[0])
    print ("Title:  " + row[1])
