# word = "balloon"

# new = {}

# for w in word:

#     if(w in new):

#         print(new)
#         break

#     else:  

#         new[w] = 1


# def first_recursive_char(word):

#     new_dict = {}

#     for w in word:

#         if(w in new_dict):

#             return new_dict
        
#         else:

#             new_dict[w] = 1
    
#     return None

# print(first_recursive_char("hello"))

word = "a man in the pnama canel"

ed = {}

rw = {}

for ch in word:

    if ch.isalpha():

        if ch in ed:

            ed[ch] += 1

        else:

            ed[ch] = 1

for k, v in ed.items():

    if(v > 1):

        print(k)