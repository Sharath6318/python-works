numbers=[150,151,153,148,153,16341,1700,16341,153]


def is_prime(n):
    
    amstrong = 0

    number = str(n)

    len_of_num = len(number)

    for d in number:

        amstrong += int(d) ** len_of_num
    
    return amstrong == n


for n in numbers:

    if is_prime(n):

        print(n)


