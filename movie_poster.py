"""
# @File    :    movie_poster.py
# @Time    :    20/04/2023 11:26
# @Author  :    Xinyao Qian
# @Description: 
"""
# 使用from..import从bs4模块导入BeautifulSoup
from bs4 import BeautifulSoup

import requests


def get_response(url, user_headers):
    response = requests.get(url, headers=user_headers)
    print(response)

    return response


def get_soup_class(response, class_name):
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    content = soup.find_all(class_=class_name)
    print(content)
    return content


# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
url = "https://movie.douban.com/top250"
response = get_response(url, headers)
get_soup_class(response, "pic")
