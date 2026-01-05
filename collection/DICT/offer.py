product = {"code":500, "title" : "t - shirt", "colors" : "blue", "size" : "m", "price" : 1500, "offer" : 10}

if "offer" in product:

    product["offer"] += 50

else:

    product["offer"] = 100


print(product)