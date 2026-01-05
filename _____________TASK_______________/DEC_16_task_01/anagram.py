def is_anagram(word_1, word_2):

    srt_val_1 = sorted(word_1) 
    srt_val_2 = sorted(word_2)

    return(srt_val_1 == srt_val_2)


print(is_anagram("act", "cat"))