# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_vowel(letter):
    return letter in "aeiouy"


def score_words(words):
    score = 0
    for word in words:
        vowels = sum(is_vowel(ch) for ch in word)
        score += 2 if vowels % 2 == 0 else 1

    return score


n = int(input())
words = input().split()
print(score_words(words))
