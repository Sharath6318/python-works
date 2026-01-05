from mysql import connector

class Vehicles:

        def __init__(self):

            try:

                self.connection = connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "Password@123",
                    database = "gosell_db"
                )

                self.cursor = self.connection.cursor()

                print('db connection OK..........')

            except Exception as e:

                print(e)

        def add_vehicle(self, **kwargs):
        
            try:

                columns = ""
                values = ""

                for k, v in kwargs.items():
                     
                     columns += k + ","
                     values += '%s' + ","

                columns = columns.rstrip(',')
                values = values.rstrip(',')
                
                query = f"""
                insert into vehicle({columns}) values({values})
                """

                data = [v for k, v in kwargs.items()]

                self.cursor.execute(query, data)

                self.connection.commit()

                print("record inserted")

            except Exception as e:
                 
                 print(e)

        def list_vehicle(self):
             
            try:
             
                query = "select * from vehicle"

                self.cursor.execute(query)

                records = self.cursor.fetchall()

                for record in records:
                    
                    print(record)

            except Exception as e:
                 
                 print(e)

        def retrive_data(self, id = None):

            try:

                  query = "select * from vehicle where id = %s"  

                  data = (id,)

                  self.cursor.execute(query, data)

                  record = self.cursor.fetchall()

                  print(record)  

            except Exception as e:
                 
                 print(e)
       
        def update_data(self, id = None, **kwargs):
            try:

                place_holder = "" 

                for k, v in kwargs.items():
                     
                     place_holder += k + "=" "%s" + ","

                place_holder = place_holder.rstrip(',')
             
                query = f"update vehicle set {place_holder} where id = {id}"

                data = [v for k, v in kwargs.items()]

                self.cursor.execute(query, data)

                self.connection.commit()

                print("Update sucessfully")

            except Exception as e:
                 
                 print(e)

        def delete_record(self, id = None):
             
            try:
                query = "delete from vehicle where id = %s"

                data = (id, )

                self.cursor.execute(query, data)

                self.connection.commit()

                print("Record deleted..........")

            except Exception as e:
                 
                 print(e)
             
vehicle_instance = Vehicles()

# vehicle_instance.add_vehicle(name = 'Yamaha',price =  170000, year = 2022, fuel_type = 'petrol',comments =  'best performance', running_km = 98000, owner_type = "single", owner = 'sharath', location = "Gudalur")

# vehicle_instance.add_vehicle(name = "KTM", price = 270000, year = 2023, fuel_type = "petrol", comments = "Good conditon", running_km = 23000, owner_type = "single", owner = "raju", location = "Thrissur")

# vehicle_instance.add_vehicle(name="Royal Enfield Classic 350",price=195000,year=2022,fuel_type="petrol",comments="Well maintained",running_km=18000,owner_type="single",owner="suresh",location="Kochi")

# vehicle_instance.add_vehicle(name="Suzuki Access 125",price=78000,year=2020,fuel_type="petrol",comments="Used for daily commute",running_km=32000,owner_type="second",owner="manoj",location="Palakkad")

# vehicle_instance.add_vehicle(name="Hyundai i20",price=620000,year=2019,fuel_type="petrol",comments="No accidents, good mileage",running_km=45000,owner_type="single",owner="vinod",location="Thrissur")

# vehicle_instance.list_vehicle()

vehicle_instance.retrive_data(id = 3)

vehicle_instance.update_data(id = 3, price = 121000)

vehicle_instance.retrive_data(id = 3)

# vehicle_instance.delete_record(id = 4)





