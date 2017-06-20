import urllib.request
import bill
import pytz
import datetime
import json



#['0200', '0500', '0800', '1100', '1400', '1700', '2000', '2300']
standard_time = [2, 5, 8, 11, 14, 17, 20, 23]

def get_api_data() :
    time_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%H')
    check_time = int(time_now) - 1
    day_calibrate = 0
    while not check_time in standard_time :
        check_time -= 1
        if check_time < 2 :
            day_calibrate = 1
            check_time = 23

    date_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%Y%m%d')
    check_date = int(date_now) - day_calibrate

    return (str(check_date), (str(check_time) + '00'))

def get_weather_data() :
    api_date, api_time = get_api_data()
    print(api_date)
    print(api_time)
    url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
    key = "serviceKey=" + bill.key
    date = "&base_date=" + api_date
    time = "&base_time=" + api_time
    nx = "&nx=97"
    ny = "&ny=76"
    numOfRows = "&numOfRows=100"
    type = "&_type=json"

    api_url = url + key + date + time + nx + ny + numOfRows + type

    data = urllib.request.urlopen(api_url).read().decode('utf8')
    parsed_json = json.loads(data)['response']['body']['items']['item']
    print(parsed_json)
    target_date = parsed_json[0]['fcstDate']
    target_time = parsed_json[0]['fcstTime']
    print(target_date)
    print(target_time)
    for one_parsed in parsed_json :
        if one_parsed['fcstDate'] == target_date and one_parsed['fcstTime'] == target_time :
            print(one_parsed['category'], one_parsed['fcstValue'])



def get_dust_data() :
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?"
    sido = "sidoName=부산"
    term = "&searchCondition=HOUR"
    key = "&ServiceKey=" + bill.key
    type = "&_type=json"

    api_url = url + sido + term + key + type
    print(api_url)


if __name__ == '__main__':
    get_weather_data()
    #get_dust_data()
    #get_api_data()

