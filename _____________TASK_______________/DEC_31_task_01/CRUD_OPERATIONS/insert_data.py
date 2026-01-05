from mysql import connector

connection = connector.connect(
    host = 'localhost',
    user = 'root',
    password = "Password@123",
    database = "crudoperation"
)

cursor = connection.cursor()

query = "insert into user(user_name, email, password) values(%s, %s, %s)"

data = [
    ('arun', 'arun@gamil.com', 'arun@123'),
    ('deepa', 'deepa@gamil.com', 'deepa@123'),
    ('krshina', 'krish@gamil.com', 'krish@123'),
    ('divya', 'divya@gamil.com', 'divya@123'),
]

cursor.executemany(query, data)

connection.commit()

print("Insertion complete")

connection.close()
cursor.close()