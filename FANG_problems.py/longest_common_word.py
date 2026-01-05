# words = ["abc", "abcd", "abstract", "abstraction"]

# common_wrd = []

# for char in words[0]:

#     if all([char in wrd for wrd in words]):

#         common_wrd.append(char)

# print(''.join(common_wrd))

class Common_wrd:

    def solution(self, lst):

        for char in lst[0]:

            if all([char in wrd for wrd in lst]):

                print(char, end="") 
            
        print(" ")

wrd_instance = Common_wrd()

wrd_instance.solution(["abc", "abcd", "abstract", "abstraction"])
wrd_instance.solution(["namee", "namaa", "namuu", "namhh"])










