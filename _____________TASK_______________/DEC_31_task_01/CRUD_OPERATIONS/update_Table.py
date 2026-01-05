from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "crudoperation",
)

cursor = connection.cursor()


query = "update user set password = %s where user_name = %s"

data = ('krish@980', 'krshina')

cursor.execute(query, data)

connection.commit()

print("update sucessfully")

connection.close()
cursor.close()