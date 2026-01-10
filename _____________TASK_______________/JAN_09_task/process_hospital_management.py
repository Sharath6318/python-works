from mysql import connector

class Hospital:
    
    def __init__(self):
        
        try:

            self.connection = connector.connect(
                host = "localhost",
                user = "root",
                password = "Password@123",
                database = "hospitaldb"
            )

            self.cursor = self.connection.cursor()

            print("Connection sucessfull")

        except Exception as e:

            print(e)

    def insertpatients(self, **kwargs):
        
        try:

            columns = " "
            values = " "

            for c, v in kwargs.items():

                columns += c + ','
                values += '%s' + ','

            columns = columns.rstrip(',')
            values = values.rstrip(',')

            query = f"insert into patient({columns}) values({values})"

            data = [v for v in kwargs.values()]

            self.cursor.execute(query, data)

            self.connection.commit()

            print("Record inserted....")

        except Exception as e:

            print(e)

    def listPatients(self):

        try:

            query = "select * from patient"

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for record in records:

                print(record)

        except Exception as e:

            print(e)

    def retrivepatient(self, id = None):

        try:

            query = f"select * from patient where patient_id = {id}"

            self.cursor.execute(query)

            record = self.cursor.fetchone()

            print(record)

        except Exception as e:

            print(e)

    def update_record(self, id = None, **kwargs):

        try:

            for k, v in kwargs.items():

                placeholder = k + '=' '%s' 

            query = f"update patient set {placeholder} where patient_id = {id}"

            data = [v for k, v in kwargs.items()]

            self.cursor.execute(query, data)

            self.connection.commit()

            print("update record sucessfully")

        except Exception as e:

            print(e)

    def delete_record(self, id = None):

        try:

            query = f"delete from patient where patient_id = {id}"

            self.cursor.execute(query)

            self.connection.commit()

            print("record deleted sucessfully")

        except Exception as e:

            print(e)

hospital_instance = Hospital()

# hospital_instance.insertpatients(patient_name="Rahul", patient_age=35,  disease="Fever", gender="Male", doctor="Dr. Sharma")
# hospital_instance.insertpatients(patient_name = "Suresh", patient_age = 45, disease = "Diabetes", gender = "Male", doctor = "Dr. Kumar")
# hospital_instance.insertpatients(patient_name="Anita",patient_age=28,disease="Cold",gender="Female",doctor="Dr. Ramesh")
# hospital_instance.insertpatients(patient_name="Priya",patient_age=32,disease="Migraine",gender="Female",doctor="Dr. Anjali")

# hospital_instance.listPatients()

hospital_instance.retrivepatient(id = 3)

# hospital_instance.update_record(id = 3, patient_age = 29)

# hospital_instance.delete_record(id = "2")