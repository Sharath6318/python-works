Menu_items = {
    "idle set" : 30,
    "dosa set" : 35,
    "biriyani" : 180,
    "normal food" : 90,
    "chinees" : 200,
    "butter nan" : 120,
    "Rotti" : 60,
}

# for item in Menu_items.keys():

#     print(item)

# for k,v in Menu_items.items():

#     if(v < 50):

#         print(k)


# items_price = Menu_items.get("fried rice", 0)
# print(items_price)

if "Rooti" in Menu_items:

    Menu_items["Rotti"] += 50

print(Menu_items)




