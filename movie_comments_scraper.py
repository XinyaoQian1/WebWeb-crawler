"""
# @File    :    movie_comments_scraper.py
# @Time    :    16/04/2023 11:44
# @Author  :    Xinyao Qian
# @Description:  scrape the comments of a movie in a webpage
"""
import requests
import jieba
from collections import defaultdict
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/subject/2129039/comments?sort=new_score&status=P'
# failed request
# response = requests.get(url)
# print(response.request.headers)


# set user-agent
# test_header = {"User-Agent": "浏览器类型"}
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0"
test_header = {"User-Agent": user_agent}
response2 = requests.get(url, headers=test_header)
# print(response2.request.headers)
# print(response2.text[12000:20000])
soup = BeautifulSoup(response2.text, "lxml")
# Find all <span> tags with class="short"
short_spans = soup.find_all('span', class_='short')
# for comments in short_spans:
#     print(comments.text)
comments = [c.text for c in short_spans]
# print(comments)
word_freq = defaultdict(int)
def count_word_frequencies(word_list):
    for word in word_list:
        if len(word) == 1:
            continue
        word_freq[word] += 1

for c in short_spans:
    c = c.text

    words = jieba.lcut(c)
    count_word_frequencies(words)

word_freq = sorted(word_freq.items(), key=lambda x:x[1], reverse=True)
print(word_freq)


