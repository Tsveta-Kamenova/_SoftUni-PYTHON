import sqlite3

inputUser = (555, "INSERT INTO user VALUES (3, 'ivan' ;DROP TABLE user;')")

with sqlite3.connect('livedemo.sqlite') as connection:
    cursor = connection.cursor()
    cursor.execute('INSERT INTO user VALUES (?, ?)', inputUser)

    cursor.execute('SELECT * FROM user')
    print(cursor.fetchall())


#   result = cursor.fetchall()
#   print(result)

#    cursor.executescript('''
#        CREATE TABLE user (
#        Id INT UNIQUE NOT NULL,
#        Name VARCHAR (50)
#       );
#
#       INSERT INTO user
#        VALUES
#        (1, 'ivan'),
#        (2, 'gosho'),
#        (3, 'stamat');
#    ''')
#   connection.commit()
