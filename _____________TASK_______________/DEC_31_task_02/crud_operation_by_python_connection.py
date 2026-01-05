from mysql import connector

class products:

    def __init__(self):
         
        try:
         
            self.connection = connector.connect(
                host = "localhost",
                user = "root",
                password = "Password@123",
                database = 'productsdb'
            )

            self.cursor = self.connection.cursor()

            print('Connection ok...........')
    
        except Exception as e:

            print(e)

    def crate_products_table(self):

        query = """create table productsData(
            product_id int primary key auto_increment,
            product_name varchar(100),
            category varchar(50),
            price int,
            stock int,
            added_Date date
        )"""

        self.cursor.execute(query)

        self.connection.commit()

        print("Table created sucessfully................")

    def add_product(self, **kwargs):

        try:

            columns = ''
            values = ''

            for k, v in kwargs.items():

                columns += k + ','
                values += '%s' + ','

            columns = columns.rstrip(',')
            values = values.rstrip(',')

            query = f"""insert into productsData({columns}) values({values})"""
            
            data = [v for k, v in kwargs.items()]
            
            self.cursor.execute(query, data)

            self.connection.commit()

            print('Product added...........')

        except Exception as e:

            print(e)

    def list_product(self):

        query = "select * from productsData"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for record in records:

            print(record)

    def retrive_product(self, id = None):
        try:

            query = f"select * from productsData where product_id = {id}"

            self.cursor.execute(query)

            record = self.cursor.fetchone()

            print(record)
            
        except Exception as e:

            print(e)

    def update_data(self, id = None, **kwargs):

        try:

            placeholder = ""

            for k, v in kwargs.items():

                placeholder += k + '=' '%s' + ','

            placeholder = placeholder.rstrip(',')

            query = f"update productsData set {placeholder} where product_id = {id}"

            data = [v for k, v in kwargs.items()]

            self.cursor.execute(query, data)

            self.connection.commit()

            print("Update record..........")

        except Exception as e:

            print(e)

    def delete_data(self, id = None):

        try:

            query = f"delete from productsData where product_id = {id}"

            self.cursor.execute(query)

            self.connection.commit()

            print("Record deleted.........")

        except Exception as e:

            print(e)

product_instance = products()

# product_instance.crate_products_table()

# product_instance.add_product(product_name = 'Laptop', category =  = 'Electronics', price = 60000, stock = 10, added_Date = '2024-01-05')
# product_instance.add_product(product_name = 'Mobile Phone', category = 'Electronics',price =  25000, stock = 25, added_Date = '2024-01-12')
# product_instance.add_product(product_name = 'Office Chair', category = 'Furniture',price =  8000, stock = 15, added_Date = '2024-02-01')
# product_instance.add_product(product_name = 'Dining Table', category = 'Furniture',price =  20000, stock = 5, added_Date = '2024-02-18')
# product_instance.add_product(product_name = 'Running Shoes',category =  'Footwear', price = 4500, stock = 30, added_Date = '2024-03-10')
# product_instance.add_product(product_name = 'T-Shirt',category =  'Clothing',price =  1200, stock = 50, added_Date = '2024-03-25')
# product_instance.add_product(product_name = 'Mixer Grinder',category =  'Home Appliances',price =  5500, stock = 12, added_Date = '2024-04-08')

# product_instance.list_product()

# product_instance.retrive_product(id = 5)

# product_instance.update_data(id = 5, stock = 25)

# product_instance.delete_data(id = 3)

