# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def get_naver_top_lank() :
    req = requests.get('http://datalab.naver.com/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    all_titles = soup.select('.keyword_rank.select_date')

    titles = []

    for top_titles in all_titles :
        for title in top_titles.select('.title') :
            titles.append(title.text)

    return titles
#print(titles)

def get_naver_dust() :
    req = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    all_dust_data = soup.select('.tb_scroll')

    for local_dust in all_dust_data :
        for dust in local_dust.find_all('tr') :
            if dust.text.find('대구') == 1 :
                daegu_dust = dust.text.strip()
                print(daegu_dust)
                hour_data = daegu_dust.split(' ')[1]
                print(hour_data)

def get_naver_weather() :
    req = requests.get('https://search.naver.com/search.naver?where=nexearch&query=%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C%EC%A3%BC%EA%B0%84%EB%82%A0%EC%94%A8&sm=tab_drt&ie=utf8')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    all_weather_data = soup.select('.rw_tr1')
    for daily_weather in all_weather_data :
        for weather in daily_weather.find_all('td'):
            print(weather.text)


def get_naver_news() :
    req = requests.get('http://news.naver.com/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    all_news_data = soup.select('#pan_today_main_news')

    for top_news in all_news_data :
        for news in top_news.select('.newsnow_tx_inner') :
            news_title = news.text.strip('\n')
            if news_title != '영상' :
                print(news_title)


if __name__ == '__main__':
    get_naver_news()



