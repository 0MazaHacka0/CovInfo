from requests import get
from re import findall
from bs4 import BeautifulSoup
import requests

req = requests.get(
    'https://covid19.rosminzdrav.ru/news/')
soup = BeautifulSoup(req.text, "lxml")


def get_news():
    res = []
    all_news = soup.find_all("div", class_="news_wrapper")
    for current_block in all_news:
        for current_new in current_block.find_all('a'):
            tmp = []
            tmp.append(current_new['title'])
            tmp.append(current_new['href'])
            for time in current_new.find_all('time'):
                tmp.append(time.text)
            res.append(tmp)
    return res
