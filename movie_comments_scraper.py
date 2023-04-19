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
from pyecharts.charts import WordCloud

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


print(type(word_freq))


# 创建WordCloud对象，赋值给wordCloud
wordCloud = WordCloud()

# 使用add()函数，series_name的值设置为空
# data_pair的值为字典wordDict转换成由元组组成的列表；
# 将word_size_range的值设置为[20,80]。
wordCloud.add(series_name = "", data_pair = word_freq.items(), word_size_range = [20,80])

# 使用wordCloud.render()存储文件，设置文件名为wordcloud.html
wordCloud.render("wordcloud.html")

# 使用print输出 success
print("success")