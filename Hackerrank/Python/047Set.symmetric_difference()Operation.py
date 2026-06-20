# Enter your code here. Read input from STDIN. Print output to STDOUT

english_news = int(input())
english_news_set = set(map(int, input().split()))
french_news = int(input())
french_news_set = set(map(int, input().split()))

symmetric_difference_set = english_news_set.symmetric_difference(
    french_news_set)
print(len(symmetric_difference_set))
