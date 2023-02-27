"""
# @File    :    main.py
# @Time    :    27/02/2023 12:08
# @Author  :    Xinyao Qian
# @Description: 
"""
import requests

url = 'https://nocturne-spider.baicizhan.com/2020/07/29/example-post-3/'

response = requests.get(url)

print(response)