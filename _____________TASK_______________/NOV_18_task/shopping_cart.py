cart1 = {"Milk", "Bread", "Eggs", "Butter"} 
cart2 = {"Bread", "Juice", "Eggs", "Cheese"}


common_purchase_item = cart1.intersection(cart2)

item_in_1_not_in_2 = cart1.difference(cart2)

item_in_2_not_in_1 = cart2.difference(cart1)

bougth_atleast_one = cart1.union(cart2)

print(f"items both customers bought : {common_purchase_item}")

print(f"items bought only by Customer 1 : {item_in_1_not_in_2}")

print(f"items bought only by Customer 2 : {item_in_2_not_in_1}")

print(f"items bought by at least one customer : {bougth_atleast_one}")
