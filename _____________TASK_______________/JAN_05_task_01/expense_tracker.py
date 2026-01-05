from mysql import connector

class expence_tracker:

    def __init__(self):

        try:
        
            self.connection = connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'Password@123',
                database = "expensedb"
            )

            self.cursor = self.connection.cursor()

            print("Connection sucessfully.....")

        except Exception as e:

            print(e)

    def create_table(self):

        try:

            query = """create table expenses(
            id int primary key auto_increment,
            title varchar(100) not null,
            amount decimal(5, 2) not null,
            category varchar(30),
            created_at datetime default current_timestamp,
            priority enum('need', 'want'),
            payment_method enum('gpay', 'phonepay', 'cash', 'card')
            )"""

            self.cursor.execute(query)

            self.connection.commit()

            print('Table created sucessfully..')

        except Exception as e:

            print(e)

    def insert_record(self, **kwargs):

        columns = ""
        values = ""

        for k, v in kwargs.items():

            columns += k + ','
            values += '%s' + ','

        columns = columns.rstrip(',')
        values = values.rstrip(',')

        query = f"insert into expenses({columns}) values({values})"

        data = [v for k, v in kwargs.items()]

        self.cursor.execute(query, data)

        self.connection.commit()

        print("Record insrted...")

    def list_records(self):

        query = "select * from expenses"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for record in records:

            print(record)

    def retrive_record(self, id = None):

        query = f"select * from expenses where id = {id}"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        for rec in record:

            print(rec)

    def update_record(self, id = None, **kwargs):
        try:

            for k, v in kwargs.items():

                placeholder = k + '=' '%s'

            query = f"update expenses set {placeholder} where id = {id}"

            data = [v for k, v in kwargs.items()]

            self.cursor.execute(query, data)

            self.connection.commit()

            print("Update record sucessfully")

        except Exception as e:

            print(e)

    def delete_record(self, id = None):

        query = f"delete from expenses where id = {id}"

        self.cursor.execute(query)

        self.connection.commit()

        print('Record deleted sucessfully.........')

expence_instance = expence_tracker()

# expence_instance.create_table()

# expence_instance.insert_record(title = 'breakfast', amount = 120, category = 'food', priority = 'need', payment_method = 'cash')
# expence_instance.insert_record(title = 'bus ticket', amount = 50 ,category = 'travel',priority = 'need', payment_method = 'cash')
# expence_instance.insert_record(title = 'petrol', amount = 500 ,category = 'fuel',priority = 'need',payment_method = 'gpay')
# expence_instance.insert_record(title = 'doctor visit', amount = 800 ,category = 'health',priority = 'need',payment_method = 'phonepay')
# expence_instance.insert_record(title = 'electricity bill', amount = 150 ,category = 'bills',priority = 'need',payment_method = 'gpay')
# expence_instance.insert_record(title = 'lunch', amount = 200 ,category = 'food',priority = 'need',payment_method = 'card')

# expence_instance.list_records()

# expence_instance.retrive_record(id = 3)

# expence_instance.update_record(id = 3, payment_method = 'gpay')

# expence_instance.delete_record(id = 7)





