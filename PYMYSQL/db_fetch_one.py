from mysql import connector

connection = connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Password@123',
    database = 'tripwisedb'
)

cursor = connection.cursor()

query = "select * from user where id = %s"

data = (4,)

cursor.execute(query, data)

record = cursor.fetchone()

print(record)   

connection.close()
cursor.close()