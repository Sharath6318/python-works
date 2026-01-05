colors = {"red", "green", "orange", "pink", "gray"}

def add_rmv(colors):

    colors.add("blue")

    colors.discard("green")

    colors.discard("yellow")

    print(colors)

add_rmv(colors)