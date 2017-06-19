import urllib.request
import bill
import pytz
import datetime
import string


url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
key = "serviceKey=" + bill.key
date = "&base_date=20170608"
time = "&base_time=2000"
nx = "&nx=97"
ny = "&ny=76"
numOfRows="&numOfRows=100"
type = "&_type=json"

#['0200', '0500', '0800', '1100', '1400', '1700', '2000', '2300']
api_time = [2, 5, 8, 11, 14, 17, 20, 23]

def get_api_data() :
    time_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%H')
    check_time = int(time_now) - 1
    day_calibrate = 0
    while not check_time in api_time :
        check_time -= 1
        if check_time < 2 :
            day_calibrate = 1
            check_time = 23

    print(check_time in api_time)
    print(check_time)

    date_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%Y%m%d')
    check_date = int(date_now) - day_calibrate
    print(str(check_date))


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

    #now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).isoformat()  # get Seoul time
    time_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%H')
    print(int(time_now)-1)

    #date = date + str(now[:10]).replace('-', '')
    #time = time + str(now[11:13]) + "00"

    #api_url = url + sido + term + key + type
    #print(api_url)



if __name__ == '__main__':
    #get_weather_data()
    #get_dust_data()
    get_api_data()

