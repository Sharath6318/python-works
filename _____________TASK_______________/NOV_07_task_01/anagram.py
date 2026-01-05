

# def is_anagram(word_1, word_2):

#     srt_val_1 = sorted(word_1) # sort(value, reversed = false) for decending order 
#     srt_val_2 = sorted(word_2)

#     return(srt_val_1 == srt_val_2)


# print(is_anagram("actt", "cat"))
# print(is_anagram("act", "cat"))


# solution - 02


def is_anagram(word1, word2):
    
    is_anagram_word = True

    if(len(word1) != len(word2)):

        return False

    for ch in word1: #c

        word_1_ch_count = word1.count(ch) #1
        word_2_ch_count = word2.count(ch) #1

        if(word_1_ch_count != word_2_ch_count): 

            is_anagram_word = False

    return is_anagram_word

print(is_anagram("cat", "act"))

            