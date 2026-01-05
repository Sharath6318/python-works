word = "abcdcdbaabcd"
sub = "aa"

count = 0

for i in range(0, 11):

    sliced_wrd = word[i: i + 2]

    if(sliced_wrd == sub):

        count += 1

print(count)
