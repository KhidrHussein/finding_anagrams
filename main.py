# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    word1_len = len(word1)
    word2_len = len(word2)
    if word1_len == word2_len:
        sorted_word1 = sorted(word1.lower())
        sorted_word2 = sorted(word2.lower())
        if sorted_word1 == sorted_word2:
            print(True)
    else:
        print(False)


def find_palindromes(word):
    # [assignment] Add your code here
    reversed_word = word[::-1].lower()
    if reversed_word == word:
        print("True")
    else:
        print("False")


find_anagrams("meat", "team")