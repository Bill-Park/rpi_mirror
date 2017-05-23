import urllib.request
import bill
import pytz
import datetime


url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
key = "serviceKey=" + bill.key
date = "&base_date=20170523"
time = "&base_time=2100"
nx = "&nx=97"
ny = "&ny=76"
type = "&_type=json"

def get_weather_data() :
    api_url = url + key + date + time + nx + ny + type
    print(api_url)

    data = urllib.request.urlopen(api_url).read()
    print(data)

def get_dust_data() :
    url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
    key = "serviceKey=" + bill.key
    date = "&base_date="
    time = "&base_time="
    nx = "&nx=97"
    ny = "&ny=76"
    type = "&_type=json"

    now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).isoformat()  # get Seoul time

    date = date + str(now[:10]).replace('-', '')
    time = time + str(now[11:13]) + "00"

    api_url = url + key + date + time + nx + ny + type
    print(api_url)



if __name__ == '__main__':
    #get_weather_data()
    get_dust_data()

