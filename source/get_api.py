import urllib.request
import bill
import pytz
import datetime


url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
key = "serviceKey=" + bill.key
date = "&base_date=20170608"
time = "&base_time=2000"
nx = "&nx=97"
ny = "&ny=76"
numOfRows="&numOfRows=100"
type = "&_type=json"

['0200', '0500', '0800', '1100', '1400', '1700', '2000', '2300']

def get_weather_data() :
    api_url = url + key + date + time + nx + ny + numOfRows + type
    print(api_url)

    data = urllib.request.urlopen(api_url).read()
    print(data)

def get_dust_data() :
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?"
    sido = "sidoName=부산"
    term = "&searchCondition=HOUR"
    key = "&ServiceKey=" + bill.key
    type = "&_type=json"

    now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).isoformat()  # get Seoul time

    #date = date + str(now[:10]).replace('-', '')
    #time = time + str(now[11:13]) + "00"

    api_url = url + sido + term + key + type
    print(api_url)



if __name__ == '__main__':
    #get_weather_data()
    get_dust_data()

