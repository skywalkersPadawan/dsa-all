# Enter your code here. Read input from STDIN. Print output to STDOUT

english_news = int(input())
english_news_set = set(map(int, input().split()))
french_news = int(input())
french_news_set = set(map(int, input().split()))

# need to find the number of students who have subscribed to only english news
difference_set = english_news_set.difference(french_news_set)
# print(difference_set) will contain the roll numbers of the students who have subscribed to the english news but not the french news
print(len(difference_set))
