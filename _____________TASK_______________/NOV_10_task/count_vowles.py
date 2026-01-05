def count_vowles(str):

    vowles = "aeiou"
    count = 0

    for ch in str:

        if(ch in vowles):

            count += 1

    return count

print(count_vowles("Luminartechnolab"))

