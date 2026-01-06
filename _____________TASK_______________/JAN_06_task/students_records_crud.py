from mysql import connector

class students:

    def __init__(self):
        
        self.connection = connector.connect(
            host = "localhost",
            user = "root",
            password = "Password@123",
            database = "studentsdb"
        )

        self.cursor = self.connection.cursor()

        print("Connection sucessfully completed....")

    def create_table(self):

        try:

            query = """create table studentsRecords(
                student_id int primary key auto_increment,
                student_name varchar(100) not null,
                gender enum('male','female', 'other'),
                department varchar(100),
                year_of_study int,
                student_email varchar(200) not null unique,
                created_at datetime default current_timestamp
            )"""

            self.cursor.execute(query)

            self.connection.commit()

            print("Table created sucessfully...")
        
        except Exception as e:

            print(e)

    def insert_table_record(self, **kwargs):

        try:

            columns = ""
            values = ""

            for k, v in kwargs.items():

                columns += k + ","
                values += "%s" + ","

            columns = columns.rstrip(",")
            values = values.rstrip(',')
            
            query = f"insert into studentsRecords({columns}) values({values})"

            data = [v for v in kwargs.values()]

            self.cursor.execute(query, data)

            self.connection.commit()

            print("record inserted sucessfully....")

        except Exception as e:

            print(e)

    def list_records(self):

        query = "select * from studentsRecords"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for record in records:

            print(record)

    
    
student_instance = students()
# student_instance.create_table()
# student_instance.insert_table_record(student_name = "sumith", gender = "male", department = "IT", year_of_study = 3, student_email = "sumith123@gamil.com")
student_instance.list_records()