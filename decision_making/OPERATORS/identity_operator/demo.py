# chuck object is  pointing to the same memory location or not using in

user_fav_foods = ["biryani", "noodles"]

user1_fav_food = ["biryani", "noodles"]

print(user1_fav_food ==  user_fav_foods) #true  compare values

print(user_fav_foods is user1_fav_food) #false  compare memory location

person1_fav_food = "biriyani"

person2_fav_food = "biriyani"

print(person1_fav_food is person2_fav_food) #true because small string have same memory location

