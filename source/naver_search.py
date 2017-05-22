import requests
from bs4 import BeautifulSoup

req = requests.get('http://datalab.naver.com/')

html = req.text

soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    '.keyword_rank.select_date'
    )
#keyword_rank select_date
#'.rank_list'
# my_titles는 list 객체
print(my_titles)

for title in my_titles:
    print(title.select('.title'))
    # Tag안의 텍스트
    #print(type(title.text))
    #if title.text :
    #    print(title.text)
    # Tag의 속성을 가져오기(ex: href속성)
    #print(title.get('href'))

