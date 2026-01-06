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

    def update_record(self, student_id = None, **kwargs):

        try:

            for k, v in kwargs.items():

                placeholder = k + '=' '%s'

            query = f"update studentsRecords set {placeholder} where student_id = {student_id}"

            data = [v for k, v in kwargs.items()]

            self.cursor.execute(query, data)

            self.connection.commit()

            print("record updated sucessfully")

        except Exception as e:

            print(e)
        
    def delete_record(self, id = None):
        try:

            query = f"delete from studentsRecords where student_id = {id}"

            self.cursor.execute(query)

            self.connection.commit()

            print("Record deleted sucessfully")

        except Exception as e:

            print(e)
    
student_instance = students()
# student_instance.create_table()
# student_instance.insert_table_record(student_name = "sumith", gender = "male", department = "IT", year_of_study = 3, student_email = "sumith123@gamil.com")
# student_instance.insert_table_record(student_name="arjun",gender="male",department="CSE",year_of_study=2,student_email="arjun.cse@gmail.com")
# student_instance.insert_table_record(student_name="meena",gender="female",department="ECE",year_of_study=4,student_email="meena.ece@gmail.com")
# student_instance.insert_table_record(student_name="rahul",gender="male",department="MECH",year_of_study=1,student_email="rahul.mech@gmail.com")
# student_instance.insert_table_record(student_name="priya",gender="female",year_of_study=3,student_email="priya.it@gmail.com")
student_instance.list_records()

# student_instance.update_record(student_id = 1, year_of_study = 3)
# student_instance.delete_record(id = 5)



