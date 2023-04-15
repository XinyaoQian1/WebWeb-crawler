"""
# @File    :    em_tag_scraper.py
# @Time    :    15/04/2023 10:38
# @Author  :    Xinyao Qian
# @Description: get the words in webpage
"""

# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page to scrape
url = "https://nocturne-spider.baicizhan.com/2020/08/07/1/"

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html = response.text

# Create a BeautifulSoup object from the HTML content, using the lxml parser
soup = BeautifulSoup(html, "lxml")

# Find all occurrences of the <em> tag in the HTML content
ps = soup.find_all(name="em")

# Print the results
print(ps)


# get the first 1000 char of the response
# html = response.text[:1000]

#

# practice using beautifulsoup
#
# html = '''
# <title>网络爬虫课程</title>
# <body>
#     <h1 align="center">我的第一个标题-居中显示</h1>
#     <h2>我的第二个标题，不居中显示</h2>
#     <p>我的第一个段落
#     </p>
# '''
# # html is the markup, "lxml" is the parser
# soup = BeautifulSoup(html,"lxml")
#
# print(soup)