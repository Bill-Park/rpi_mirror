import requests
from bs4 import BeautifulSoup

req = requests.get('http://news.naver.com/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

all_news_data = soup.select('#pan_today_main_news')

for top_news in all_news_data:
    for news in top_news.select('.newsnow_tx_inner'):
        news_title = news.text.strip('\n')
        if news_title != '영상':
            print(news_title)
