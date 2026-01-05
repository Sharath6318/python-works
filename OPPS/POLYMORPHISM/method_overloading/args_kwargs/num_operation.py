# *args(*arguments), **kwargs(**keywordarguments)
def operation(*args, **kwargs):

    op = kwargs.get("key")

    if op == "max":

        print(max(args))

    else:

        print(min(args))

operation(10, 20, 30, key = "max")
operation(10, 20, 30, key = "min")