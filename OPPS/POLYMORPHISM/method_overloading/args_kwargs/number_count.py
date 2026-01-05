class Numbercount:

    def solution(*args, **kargss):

        if kargss.get("value") in args:

            count_val = args.count(kargss.get("value"))

            return(count_val)
        
        else:

            return("Not a valid number")

num_const_instance = Numbercount()

print(num_const_instance.solution(10, 20, 30, 40, 50,10, value = 10))

