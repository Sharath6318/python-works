from mysql import connector

connection = connector.connect(
    host = 'localhost',
    user = 'root',
    password = "Password@123",
    database = 'tripwisedb'
)

cursor = connection.cursor()

query = """
    insert into user(name, email, password) values(%s, %s, %s)
"""

# data = ('vibin', 'vibin@gamil.com', 'vib@123')

data = [
    ('reena', 'rena@gmail.com', 'ren@123'),
    ('teena', 'tena@gmail.com', 'tena@123'),
    ('deepa', 'deepa@gmail.com', 'depa@123'),
    ('shela', 'shela@gmail.com', 'shela@123'),
]

cursor.executemany(query, data)

connection.commit()

print("Query executed...")

connection.close()
cursor.close()



