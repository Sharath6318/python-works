from mysql import connector

class Library:

    def __init__(self):
        
        try:

            self.connection = connector.connect(
                host = "localhost",
                user = "root",
                password = "Password@123",
                database = "librarydb"
            )

            self.cursor = self.connection.cursor()

            print("Connection sucessfully")

        except Exception as e:

            print(e)

    def create_table(self):
        try:

            query = """create table libraryManagement(
                member_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE,
                phone VARCHAR(15),
                department VARCHAR(50),
                join_date =  DATE
            )"""

            self.cursor.execute(query)

            self.connection.commit()

            print("Table created sucessfully..........")

        except Exception as e:

            print(e)

    def insert_table(self, **kwargs):

        try:

            columns = " "
            values = " "

            for k in kwargs.keys():

                columns += k + ","
                values += "%s" + ","

            columns = columns.rstrip(',')
            values = values.rstrip(',')

            query = f"insert into libraryManagement({columns}) values({values})"

            data = [v for v in kwargs.values()]

            self.cursor.execute(query, data)

            self.connection.commit()

            print("Record inserted sucessfully........")

        except Exception as e:

            print(e)

    def list_record(self):

        try:
            query = "select * from libraryManagement"

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for record in records:

                print(record)

        except Exception as e:

            print(e)

    def retrive_record(self, id = None):

        query = f"select * from libraryManagement where member_id = {id}"

        self.cursor.execute(query)

        record = self.cursor.fetchone()

        print(record)

    def update_record(self, id = None, **kwargs):

        try:

            placeholder = ""

            for k in kwargs.keys():

                placeholder += k + '=' '%s'

            query = f"update libraryManagement set {placeholder} where member_id = {id}"

            data = [v for v in kwargs.values()]

            self.cursor.execute(query, data)

            self.connection.commit()

            print("record updated sucessfully...........")

        except Exception as e:

            print(e)

    def delete_record(self, id = None):

        try:

            query = f"delete from libraryManagement where member_id = {id}"

            self.cursor.execute(query)

            self.connection.commit()

            print("Record deleted sucessfully..........")

        except Exception as e:

            print(e)

library_instance = Library()

# library_instance.create_table()

# library_instance.insert_table(name = 'Rahul Kumar', email = 'rahul@gmail.com', phone = '9876543210', department = 'IT', join_date = '2024-06-10')
# library_instance.insert_table(name = 'Anjali Sharma', email = 'anjali@gmail.com', phone = '9123456789', department = 'CSE', join_date = '2024-07-01')
# library_instance.insert_table(name = 'Suresh Raj', email = 'suresh@gmail.com', phone = '9012345678', department = 'ECE', join_date = '2024-07-15')

# library_instance.list_record()

# library_instance.retrive_record(id = 3)

# library_instance.update_record(id = 3, department = "MECH")


