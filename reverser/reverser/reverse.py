def reverse(word):
    letter = ""
    r = ""
    for i in range(len(word) - 1, -1, -1):
        letter = word[i]
        r = r + letter
    return r
