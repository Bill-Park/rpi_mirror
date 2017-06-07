from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_raw_data():
    now = datetime.now()
    today_str = "{:04d}-{:02d}-{:02d}".format(now.year, now.month, now.day)
    g_URL = "http://www.airkorea.or.kr/sido_compare_p01?itemCode=10007&ymd={}%2023&areaCode=031".format(today_str)
    html_str = urlopen(g_URL).read().decode('utf-8')
    return html_str

def get_data_where(location_):
    html = get_raw_data()
    soup = BeautifulSoup(html)
    trs = [tr for tr in soup.find_all('tr') if location_ in tr.text]
    if trs:
        data = [x for x in trs[0].text.strip().split('n')]
        data[1:] = [int(x) for x in data[1:] if x != '-']
        return data
    return None

def print_data_where(location_):
    data = get_data_where(location_)
    for i, d in enumerate(data[1:]):
        print("{}시: {}".format(i+1, d))


print_data_where("통진")