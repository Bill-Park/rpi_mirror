import requests
from bs4 import BeautifulSoup

def get_naver_top_lank() :
    req = requests.get('http://datalab.naver.com/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    all_titles = soup.select(
        '.keyword_rank.select_date'
        )

    titles = []

    for top_titles in all_titles :
        for title in top_titles.select('.title') :
            titles.append(title.text)

    return titles
#print(titles)