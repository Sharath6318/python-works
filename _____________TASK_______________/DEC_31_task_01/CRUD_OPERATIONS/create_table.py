from mysql import connector

connection = connector.connect(
    host = 'localhost',
    user = 'root',
    password = "Password@123",
    database = "crudoperation"
)

cursor = connection.cursor()

# create table............

query = """
create table user(
    user_id int primary key auto_increment,
    user_name varchar(100) not null,
    email varchar(100) not null unique,
    password varchar(15) not null,
    created_at datetime default current_timestamp
)"""

cursor.execute(query)

print("table created..")

connection.close()
cursor.close()

