import urllib.request
import bill

url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
key = bill.key
date = "&base_date=20170516"
time = "&base_time=2000"
nx = "&nx=97"
ny = "&ny=76"
type = "&_type=json"


api_url = url + key + date + time + nx + ny + type
print(api_url)

data = urllib.request.urlopen(api_url).read()
print(data)

