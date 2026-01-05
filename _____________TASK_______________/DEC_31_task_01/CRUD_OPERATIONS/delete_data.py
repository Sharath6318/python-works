from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = 'root',
    password = "Password@123",
    database = "crudoperation"
)

cursor = connection.cursor()

query = "delete from user where user_id = %s"

data = (2,)

cursor.execute(query, data)

connection.commit()

print("data deleted.............")

connection.close()
cursor.close()